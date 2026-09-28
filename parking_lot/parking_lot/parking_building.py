"""
===============================================================================
ParkingBuilding
===============================================================================

Purpose
-------
The ParkingBuilding is the collection of all levels. It is the place
where the question "WHERE should this vehicle park?" is answered.

Responsibilities
----------------
1. allocate(vehicle)
   Walk the levels in order, find the first level that has a free spot
   for the vehicle's type, park there and issue a Ticket.

2. release(ticket)
   Use the level and spot stored on the Ticket to free the spot.

What It Does NOT Do
-------------------
1. It does not compute prices   -> ExitGate + CostComputation
2. It does not collect money    -> Payment
3. It does not pick a spot on a level -> ParkingSpotManager + strategy

Each class has one reason to change (Single Responsibility Principle).

Allocation Algorithm
--------------------

for each level (level 1, level 2, ...):
    if level has a free spot for this vehicle type:
        spot = level.park(vehicle type)
        if spot was actually obtained:
            return Ticket(vehicle, level, spot)
raise "Parking Full"

Why check "spot is not None" after has_availability()?
    Between the check and the park call, another thread may have taken
    the last spot. In that case park() returns None and we simply try
    the next level instead of failing.

Level order means lower levels fill first. To prefer, say, the level
with the most free spots, only this method would change.
===============================================================================
"""

from .parking_level import ParkingLevel
from vehicle import Vehicle
from ticket import Ticket


class ParkingBuilding:
    """
    Aggregate of all ParkingLevels.

    Allocates spots on entry and releases them on exit.
    """

    def __init__(self, levels: list[ParkingLevel]):
        """
        Args:
            levels (list[ParkingLevel]): Levels in the order they should
                be tried when allocating.
        """
        self.levels = levels

    def allocate(self, vehicle: Vehicle) -> Ticket:
        """
        Finds a spot for the vehicle and issues a Ticket.

        Args:
            vehicle (Vehicle): The arriving vehicle.

        Returns:
            Ticket: Records vehicle, level, spot and entry time.

        Raises:
            RuntimeError: If no level has a free spot for this type.
        """
        for level in self.levels:
            if level.has_availability(vehicle.get_vehicle_type()):
                spot = level.park(vehicle.get_vehicle_type())

                if spot is not None:
                    ticket = Ticket(vehicle, level, spot)

                    print(
                        f"Parking allocated at level: "
                        f"{level.get_level_number()} "
                        f"spot: {spot.get_spot_id()}"
                    )

                    return ticket

        raise RuntimeError("Parking Full")

    def release(self, ticket: Ticket) -> None:
        """
        Frees the spot recorded on the ticket.

        No searching is needed: the ticket already points to the exact
        level and spot.

        Args:
            ticket (Ticket): Ticket issued at entry.

        Returns:
            None
        """
        ticket.get_level().un_park(
            ticket.get_vehicle().get_vehicle_type(),
            ticket.get_spot()
        )
