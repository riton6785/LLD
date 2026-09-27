"""
===============================================================================
ParkingSpot
===============================================================================

Purpose
-------
A ParkingSpot is the smallest physical unit of the parking lot: one place
where one vehicle can stand. It only tracks two things:

    spot_id   -> human readable id, e.g. "L1-S3" (Level 1, Spot 3)
    is_free   -> True when empty, False when a vehicle is parked

State Diagram
-------------

        occupy_spot()
    FREE -------------> OCCUPIED
     ^                     |
     |                     |
     +---------------------+
         release_spot()

Design Decision
---------------
A spot does NOT decide who may park in it, and does NOT protect itself
against two cars grabbing it at the same time.

Those responsibilities belong to the ParkingSpotManager that owns it:

1. It groups spots meant for the same vehicle type.
2. It wraps "find a free spot + occupy it" in a lock, so the
   FREE -> OCCUPIED transition is thread-safe.

Keeping the spot "dumb" keeps it reusable and easy to test.
===============================================================================
"""


class ParkingSpot:
    """
    Entity representing one physical parking place.

    A new spot always starts FREE.
    """

    def __init__(self, spot_id):
        """
        Args:
            spot_id (str): Identifier printed on the ticket, e.g. "L2-S1".
        """
        self.spot_id = spot_id
        self.is_free = True

    def is_spot_free(self):
        """
        Returns:
            bool: True if no vehicle is currently parked here.
        """
        return self.is_free

    def occupy_spot(self):
        """
        Marks the spot as OCCUPIED.

        Called only by ParkingSpotManager.park() while holding its lock.

        Returns:
            None
        """
        self.is_free = False

    def release_spot(self):
        """
        Marks the spot as FREE again.

        Called only by ParkingSpotManager.un_park() while holding its lock.

        Returns:
            None
        """
        self.is_free = True

    def get_spot_id(self):
        """
        Returns:
            str: Spot identifier, e.g. "L1-S1".
        """
        return self.spot_id
