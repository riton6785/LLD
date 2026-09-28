"""
===============================================================================
ParkingSpotLookupStrategy  (Strategy Pattern)
===============================================================================

Definition
----------
Strategy is a Behavioral Design Pattern that defines a family of
algorithms, puts each one in its own class, and makes them
interchangeable at runtime.

Problem Statement
-----------------
"Which free spot should a vehicle get?" has many valid answers:

    - the first free spot
    - a random free spot
    - the spot nearest to the entrance
    - the spot nearest to the lift

Without Strategy, ParkingSpotManager would contain all of them:

    if mode == "first":
        ...
    elif mode == "nearest":
        ...
    elif mode == "random":
        ...

Every new rule means editing (and re-testing) the manager.

Solution
--------
The manager only asks a strategy object:

    spot = self.strategy.select_spot(self.spots)

The actual algorithm lives in a concrete strategy class, injected
through the constructor (composition over inheritance).

Benefits
--------
1. Open/Closed Principle
   New lookup rules = new class, no change to the manager.

2. Swappable at Runtime
   Different levels / managers can use different strategies.

3. Easy Testing
   Each algorithm can be tested in isolation.

Drawbacks
---------
1. More Classes
   One class per algorithm.

2. Client Must Pick
   Someone (here: client.py) must decide which strategy to inject.

Strategy Flow
-------------

ParkingSpotManager.park()
   |
   v
strategy.select_spot(spots)     <- abstract call
   |
   v
Concrete Strategy               <- e.g. RandomLookupStrategy
   |
   v
ParkingSpot or None
===============================================================================
"""

from abc import ABC, abstractmethod
from parking_spot import ParkingSpot


class ParkingSpotLookupStrategy(ABC):
    """
    Abstract Strategy.

    Declares the single operation every spot lookup algorithm
    must implement.
    """

    @abstractmethod
    def select_spot(self, spots: list[ParkingSpot]):
        """
        Chooses one FREE spot from the given list.

        The strategy only CHOOSES; it must not occupy the spot.
        Occupying is done by the ParkingSpotManager under its lock.

        Args:
            spots (list[ParkingSpot]): All spots owned by one manager.

        Returns:
            ParkingSpot | None: A free spot, or None if all are occupied.
        """
        pass
