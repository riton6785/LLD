"""
===============================================================================
RandomLookupStrategy  (Concrete Strategy)
===============================================================================

Purpose
-------
One concrete implementation of ParkingSpotLookupStrategy.

Note for Readers
----------------
Despite its name, this strategy is NOT random: it scans the list in
order and returns the FIRST free spot ("first-fit").

    spots = [L1-S1 (occupied), L1-S2 (free), L1-S3 (free)]
    select_spot(spots)  ->  L1-S2

A truly random version could look like this:

    free_spots = [s for s in spots if s.is_spot_free()]
    return random.choice(free_spots) if free_spots else None

Because both follow the same interface, either can be injected into a
ParkingSpotManager without the manager noticing -- which is exactly the
point of the Strategy Pattern.

Complexity
----------
O(n) in the number of spots owned by the manager.
===============================================================================
"""

from .parking_lookup_strategy import ParkingSpotLookupStrategy
from parking_spot import ParkingSpot


class RandomLookupStrategy(ParkingSpotLookupStrategy):
    """
    Concrete Strategy.

    Returns the first free spot in list order (first-fit).
    """

    def select_spot(self, spots: list[ParkingSpot]):
        """
        Scans spots in order and returns the first free one.

        Args:
            spots (list[ParkingSpot]): All spots owned by one manager.

        Returns:
            ParkingSpot | None: First free spot, or None if none is free.
        """
        for spot in spots:
            if spot.is_spot_free():
                return spot

        return None
