"""
===============================================================================
FourWheelerSpotManager
===============================================================================

Purpose
-------
Concrete ParkingSpotManager for cars
(VehicleType.FOUR_WHEELER).

It currently adds no behaviour of its own; all parking logic is
inherited from ParkingSpotManager.

Why Keep an "Empty" Subclass?
-----------------------------
1. Readability
   client.py clearly states which spots are for four-wheelers.

2. Extension Point
   Car specific rules (e.g. reserved EV-charging spots, handicap
   spots) can be added here without touching the two-wheeler logic.
===============================================================================
"""

from .parking_spot_manager import ParkingSpotManager
from parking_spot import ParkingSpot
from spot_lookup_strategy.parking_lookup_strategy import ParkingSpotLookupStrategy


class FourWheelerSpotManager(ParkingSpotManager):
    """
    Manages all four-wheeler spots on one level.
    """

    def __init__(self, spots: list[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        """
        Args:
            spots (list[ParkingSpot]): Four-wheeler spots on this level.
            strategy (ParkingSpotLookupStrategy): Spot selection algorithm.
        """
        super().__init__(spots, strategy)
