"""
===============================================================================
ParkingSpotManager
===============================================================================

Purpose
-------
A ParkingSpotManager owns ALL spots of ONE vehicle type on ONE level.

    Level 1
      |-- TwoWheelerSpotManager   -> [L1-S1, L1-S2]
      |-- FourWheelerSpotManager  -> [L1-S3]

It is the only class allowed to change a spot's state
(occupy / release).

Responsibilities
----------------
1. Answer "is there any free spot?"            -> has_free_spot()
2. Pick a free spot and occupy it atomically   -> park()
3. Release a spot when a vehicle leaves        -> un_park()

What It Delegates
-----------------
It does NOT decide WHICH free spot to give. That choice is delegated
to a ParkingSpotLookupStrategy (Strategy Pattern):

    spot = self.strategy.select_spot(self.spots)

Thread Safety
-------------
Imagine two cars arriving at two entrances at the same instant:

    Car A: select_spot() -> L1-S3 (free)
    Car B: select_spot() -> L1-S3 (still free!)
    Car A: occupy_spot()
    Car B: occupy_spot()           <- two cars, one spot!

This is a classic "check-then-act" race condition.

The manager prevents it by holding a lock around
"select + occupy", so only one thread at a time can run it.

An RLock (re-entrant lock) is used so a thread that already holds the
lock can acquire it again without dead-locking itself.

Why an Abstract Base Class?
---------------------------
TwoWheelerSpotManager and FourWheelerSpotManager share this behaviour
today, but each vehicle type may later need its own rules
(e.g. EV spots that need a charger check). The base class holds the
common logic; subclasses are the extension points.
===============================================================================
"""

import threading
from abc import ABC, abstractmethod
from parking_spot import ParkingSpot
from spot_lookup_strategy.parking_lookup_strategy import ParkingSpotLookupStrategy


class ParkingSpotManager(ABC):
    """
    Abstract base for managers that own spots of a single vehicle type.

    Acts as the Context in the Strategy Pattern: it holds a
    ParkingSpotLookupStrategy and delegates spot selection to it.
    """

    def __init__(self, spots: list[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        """
        Args:
            spots (list[ParkingSpot]): Spots this manager is responsible for.
            strategy (ParkingSpotLookupStrategy): Algorithm used to pick
                a free spot.
        """
        self.spots = spots
        self.strategy = strategy
        # Guards every read/write of spot state managed by this object.
        self.lock = threading.RLock()

    def park(self):
        """
        Selects a free spot with the strategy and marks it OCCUPIED.

        Selection and occupation happen inside the same lock, so no other
        thread can grab the same spot in between.

        Returns:
            ParkingSpot | None: The occupied spot, or None if full.
        """
        with self.lock:
            spot: ParkingSpot = self.strategy.select_spot(self.spots)
            if spot is None:
                return None

            spot.occupy_spot()
            return spot

    def un_park(self, spot: ParkingSpot):
        """
        Marks the given spot FREE again.

        Args:
            spot (ParkingSpot): The spot taken from the Ticket.

        Returns:
            None
        """
        with self.lock:
            spot.release_spot()

    def has_free_spot(self):
        """
        Quick availability check used by ParkingLevel before parking.

        Note: the answer can be stale by the time park() is called
        (another thread may take the last spot). That is why park()
        can still return None and callers must handle it.

        Returns:
            bool: True if at least one spot is free.
        """
        with self.lock:
            return any(spot.is_spot_free() for spot in self.spots)
