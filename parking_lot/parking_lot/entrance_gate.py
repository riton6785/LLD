"""
===============================================================================
EntranceGate
===============================================================================

Purpose
-------
The EntranceGate models the physical barrier where vehicles enter.
Its job is simple: take an arriving vehicle, get it a spot from the
building, and hand back a Ticket.

Why a Separate Class?
---------------------
Today it only forwards to ParkingBuilding.allocate(). It exists because
entry is a real-world concept with its own future responsibilities:

    - scanning the number plate
    - checking a blacklist / reservation
    - showing "FULL" on a display board
    - supporting several entrances (Gate A, Gate B, ...)

These can be added here without touching allocation logic.

The gate receives the building as a parameter instead of storing it,
so the same gate object could serve any building.

Flow
----

ParkingLot.vehicle_arrives(vehicle)
   |
   v
EntranceGate.enter(building, vehicle)
   |
   v
ParkingBuilding.allocate(vehicle)
   |
   v
Ticket
===============================================================================
"""

from ticket import Ticket
from .parking_building import ParkingBuilding
from vehicle import Vehicle


class EntranceGate:
    """
    Entry point for vehicles; issues tickets.
    """

    def enter(
    self,
    building: ParkingBuilding,
    vehicle: Vehicle
    ) -> Ticket:
        """
        Parks the vehicle and returns its ticket.

        Args:
            building (ParkingBuilding): Building to allocate a spot in.
            vehicle (Vehicle): The arriving vehicle.

        Returns:
            Ticket: Proof of parking for the driver.

        Raises:
            RuntimeError: If the building is full for this vehicle type.
        """
        return building.allocate(vehicle)
