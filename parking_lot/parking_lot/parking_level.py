"""
===============================================================================
ParkingLevel
===============================================================================

Purpose
-------
A ParkingLevel is one floor of the building. It does not own spots
directly; it owns one ParkingSpotManager PER vehicle type:

    ParkingLevel(1)
      managers = {
          VehicleType.TWO_WHEELER  : TwoWheelerSpotManager([L1-S1, L1-S2]),
          VehicleType.FOUR_WHEELER : FourWheelerSpotManager([L1-S3]),
      }

Responsibilities
----------------
1. Route a request to the right manager using the vehicle type.
2. Report availability for a vehicle type.
3. Forward park / un_park calls to that manager.

Why a Dictionary of Managers?
-----------------------------
Without it, the level would need a branch per vehicle type:

    if vehicle_type == TWO_WHEELER:
        return self.two_wheeler_manager.park()
    elif vehicle_type == FOUR_WHEELER:
        return self.four_wheeler_manager.park()

With a dictionary lookup, adding a new vehicle type is only a matter of
registering a new manager in client.py. The level code never changes.

It also lets levels differ: a level with no FOUR_WHEELER entry simply
has no car parking, and has_availability() returns False for cars.

Delegation Chain
----------------

ParkingBuilding
   |
   v
ParkingLevel          <- picks manager by VehicleType
   |
   v
ParkingSpotManager    <- picks spot via strategy, occupies it
   |
   v
ParkingSpot
===============================================================================
"""

from spot_managers.parking_spot_manager import ParkingSpotManager
from enums.vehicle_type import VehicleType


class ParkingLevel:
    """
    One floor of the parking building.

    Routes each request to the ParkingSpotManager registered for the
    vehicle's type.
    """

    def __init__(
    self,
    level_number: int,
    managers: dict[VehicleType, ParkingSpotManager]
    ):
        """
        Args:
            level_number (int): Floor number, printed when allocating.
            managers (dict[VehicleType, ParkingSpotManager]): One manager
                for every vehicle type this level supports.
        """
        self.level_number = level_number
        self.managers = managers

    def has_availability(self, vehicle_type: VehicleType) -> bool:
        """
        Checks whether this level can take a vehicle of the given type.

        Args:
            vehicle_type (VehicleType): Type of the arriving vehicle.

        Returns:
            bool: False if the level has no manager for this type or
            all its spots are occupied.
        """
        manager: ParkingSpotManager = self.managers.get(vehicle_type)

        return manager is not None and manager.has_free_spot()

    def park(self, vehicle_type: VehicleType):
        """
        Asks the matching manager to occupy a spot.

        Args:
            vehicle_type (VehicleType): Type of the arriving vehicle.

        Returns:
            ParkingSpot | None: The occupied spot, or None if the manager
            became full after the availability check.

        Raises:
            ValueError: If this level has no manager for the vehicle type.
        """
        manager: ParkingSpotManager = self.managers.get(vehicle_type)

        if manager is None:
            raise ValueError(
                f"No parking manager for vehicle type: {vehicle_type}"
            )

        return manager.park()

    def un_park(self, vehicle_type: VehicleType, spot):
        """
        Frees a spot on this level.

        Args:
            vehicle_type (VehicleType): Type of the leaving vehicle.
            spot (ParkingSpot): The spot recorded on the ticket.

        Returns:
            None
        """
        manager: ParkingSpotManager = self.managers.get(vehicle_type)

        if manager is not None:
            manager.un_park(spot)

    def get_level_number(self) -> int:
        """
        Returns:
            int: Floor number of this level.
        """
        return self.level_number
