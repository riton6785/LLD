"""
===============================================================================
Vehicle
===============================================================================

Purpose
-------
A Vehicle is the "customer" of the parking lot. It is a plain data object
(an entity) that carries two facts:

    vehicle_number  -> unique identity, e.g. "CAR-201" (the number plate)
    vehicle_type    -> a VehicleType, used to pick the right kind of spot

Design Decision
---------------
The Vehicle knows NOTHING about parking, tickets or payments.

Keeping entities free of business logic means parking rules can change
without touching this class (Single Responsibility Principle).

Who Uses It
-----------
1. ParkingLot.vehicle_arrives(vehicle)
   Entry point of the whole system.

2. ParkingBuilding.allocate(vehicle)
   Reads vehicle_type to find a matching spot.

3. Ticket
   Remembers which vehicle parked, so the exit knows which
   spot manager to release the spot to.
===============================================================================
"""


class Vehicle:
    """
    Entity representing a vehicle that wants to park.

    Example:
        car = Vehicle("CAR-201", VehicleType.FOUR_WHEELER)
    """

    def __init__(self, vehicle_number, vehicle_type):
        """
        Args:
            vehicle_number (str): Number plate / unique identifier.
            vehicle_type (VehicleType): Decides which spot type it needs.
        """
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def get_vehicle_number(self):
        """
        Returns:
            str: Number plate of the vehicle.
        """
        return self.vehicle_number

    def get_vehicle_type(self):
        """
        Used by ParkingBuilding and ParkingLevel to route the vehicle
        to the right ParkingSpotManager.

        Returns:
            VehicleType: Category of the vehicle.
        """
        return self.vehicle_type
