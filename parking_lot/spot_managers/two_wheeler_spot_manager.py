"""
===============================================================================
TwoWheelerSpotManager
===============================================================================

Purpose
-------
Concrete ParkingSpotManager for bikes and scooters
(VehicleType.TWO_WHEELER).

It currently adds no behaviour of its own; all parking logic is
inherited from ParkingSpotManager.

Why Keep an "Empty" Subclass?
-----------------------------
1. Readability
   client.py clearly states which spots are for two-wheelers.

2. Extension Point
   Two-wheeler specific rules (e.g. several bikes per spot) can be
   added here without touching the four-wheeler logic.
===============================================================================
"""

from .parking_spot_manager import ParkingSpotManager
from parking_spot import ParkingSpot
from spot_lookup_strategy.parking_lookup_strategy import ParkingSpotLookupStrategy


class TwoWheelerSpotManager(ParkingSpotManager):
    """
    Manages all two-wheeler spots on one level.
    """

    def __init__(self, spots: list[ParkingSpot], strategy: ParkingSpotLookupStrategy):
        """
        Args:
            spots (list[ParkingSpot]): Two-wheeler spots on this level.
            strategy (ParkingSpotLookupStrategy): Spot selection algorithm.
        """
        super().__init__(spots, strategy)
