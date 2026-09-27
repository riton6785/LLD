"""
===============================================================================
VehicleType (Enum)
===============================================================================

Purpose
-------
Every vehicle that enters the parking lot belongs to exactly one category.
The category decides WHICH kind of parking spot the vehicle may use:

    TWO_WHEELER   -> bikes, scooters   -> TwoWheelerSpotManager
    FOUR_WHEELER  -> cars, SUVs        -> FourWheelerSpotManager

Problem Statement
-----------------
Suppose vehicle types were plain strings:

    Vehicle("CAR-201", "FOUR_WHEELR")     # typo!

Nothing fails at creation time. The bug only shows up much later as
"Parking Full", because no level has a manager for "FOUR_WHEELR".

Solution
--------
An Enum defines a closed set of allowed values:

    Vehicle("CAR-201", VehicleType.FOUR_WHEELER)

Benefits
--------
1. Typos Fail Immediately
   VehicleType.FOUR_WHEELR raises AttributeError right away.

2. Safe Dictionary Keys
   ParkingLevel stores {VehicleType -> ParkingSpotManager}.

3. IDE Support
   Auto-completion lists every valid category.

Extending
---------
To support a new category (e.g. HEAVY_VEHICLE):

1. Add a member here.
2. Create a matching spot manager.
3. Register that manager on the levels that can host it.

No existing parking logic changes -> Open/Closed Principle.
===============================================================================
"""

from enum import Enum


class VehicleType(Enum):
    """
    The closed set of vehicle categories the parking lot understands.

    Used as the key that routes a vehicle to the correct
    ParkingSpotManager on every ParkingLevel.
    """

    TWO_WHEELER = "TWO_WHEELER"
    FOUR_WHEELER = "FOUR_WHEELER"
