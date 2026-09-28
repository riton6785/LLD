"""
===============================================================================
Ticket
===============================================================================

Purpose
-------
The Ticket is the RECEIPT handed to the driver at the entrance gate and
returned at the exit gate. It is the only link between "arriving" and
"leaving", so it must remember everything the exit needs:

    vehicle     -> who parked (its type tells us which manager to release to)
    level       -> on which ParkingLevel the vehicle is parked
    spot        -> the exact ParkingSpot that was occupied
    entry_time  -> when the vehicle entered (input for pricing)

Why Store the Level and the Spot?
---------------------------------
At exit time we must free exactly the spot that was taken.

If the ticket only held a spot id, the building would have to search
every level to find it. Holding direct references makes release O(1):

    ticket.get_level().un_park(vehicle_type, ticket.get_spot())

Why Store entry_time?
---------------------
FixedPricingStrategy ignores it, but an hourly strategy would compute:

    datetime.now() - ticket.get_entry_time()

Storing it now means new pricing strategies can be added without
changing the Ticket.

Lifecycle
---------

EntranceGate.enter()
   |
   v
ParkingBuilding.allocate()  --> creates Ticket
   |
   v
Driver keeps Ticket while parked
   |
   v
ExitGate.complete_exit(ticket)  --> price, pay, release spot
===============================================================================
"""

from datetime import datetime
from vehicle import Vehicle
from parking_lot.parking_level import ParkingLevel
from parking_spot import ParkingSpot


class Ticket:
    """
    Proof of parking, created on entry and consumed on exit.

    entry_time is stamped automatically at creation.
    """

    def __init__(
    self,
    vehicle: Vehicle,
    level: ParkingLevel,
    spot: ParkingSpot
    ):
        """
        Args:
            vehicle (Vehicle): The vehicle that parked.
            level (ParkingLevel): The level where the spot was found.
            spot (ParkingSpot): The spot that is now occupied.
        """
        self.vehicle = vehicle
        self.level = level
        self.spot = spot
        self.entry_time = datetime.now()

    def get_vehicle(self) -> Vehicle:
        """
        Returns:
            Vehicle: The vehicle this ticket was issued to.
        """
        return self.vehicle

    def get_level(self) -> ParkingLevel:
        """
        Returns:
            ParkingLevel: The level where the vehicle is parked.
        """
        return self.level

    def get_spot(self) -> ParkingSpot:
        """
        Returns:
            ParkingSpot: The exact spot occupied by the vehicle.
        """
        return self.spot

    def get_entry_time(self) -> datetime:
        """
        Returns:
            datetime: Time of entry; input for time-based pricing.
        """
        return self.entry_time
