"""
===============================================================================
ParkingLot  (Facade)
===============================================================================

Definition
----------
Facade is a Structural Design Pattern that provides one simple interface
to a complex subsystem.

Problem Statement
-----------------
Parking a car touches many objects: gates, building, levels, spot
managers, lookup strategies, pricing, payment.

Without a facade, client code would have to know and call them in the
right order:

    ticket = entrance_gate.enter(building, vehicle)
    ...
    amount = exit_gate.calculate_price(ticket)
    payment.pay(amount)
    building.release(ticket)

Solution
--------
ParkingLot hides all of that behind two operations that match how a
driver thinks about parking:

    ticket = parking_lot.vehicle_arrives(vehicle)
    parking_lot.vehicle_exits(ticket, payment)

Benefits
--------
1. Simple Client Code
   The caller needs only a Vehicle, a Ticket and a Payment.

2. Loose Coupling
   Internals (e.g. allocation rules) can change without breaking callers.

3. Single Entry Point
   A natural place for logging, metrics or a REST API later.

Composition
-----------

ParkingLot
  |-- ParkingBuilding
  |      |-- ParkingLevel (1..n)
  |             |-- ParkingSpotManager (per VehicleType)
  |                    |-- ParkingSpot (1..n)
  |                    |-- ParkingSpotLookupStrategy
  |-- EntranceGate
  |-- ExitGate
         |-- CostComputation
                |-- PricingStrategy
===============================================================================
"""

from .parking_building import ParkingBuilding
from .entrance_gate import EntranceGate
from vehicle import Vehicle
from ticket import Ticket
from .exit_gate import ExitGate
from payment.payment import Payment


class ParkingLot:
    """
    Facade over the whole parking subsystem.

    Exposes only vehicle_arrives() and vehicle_exits().
    """

    def __init__(
    self,
    building: ParkingBuilding,
    entrance_gate: EntranceGate,
    exit_gate: ExitGate
    ):
        """
        All collaborators are injected (Dependency Injection), so the
        facade never builds its own parts and can be wired differently
        in tests or other deployments.

        Args:
            building (ParkingBuilding): Levels and spots.
            entrance_gate (EntranceGate): Issues tickets.
            exit_gate (ExitGate): Prices, collects payment, releases.
        """
        self.building = building
        self.entrance_gate = entrance_gate
        self.exit_gate = exit_gate

    def vehicle_arrives(self, vehicle: Vehicle) -> Ticket:
        """
        Parks an arriving vehicle.

        Args:
            vehicle (Vehicle): The arriving vehicle.

        Returns:
            Ticket: Must be presented at exit.

        Raises:
            RuntimeError: If no spot is available for the vehicle type.
        """
        return self.entrance_gate.enter(
            self.building,
            vehicle
        )

    def vehicle_exits(
        self,
        ticket: Ticket,
        payment: Payment
    ) -> None:
        """
        Checks a vehicle out: price, pay, release spot.

        Args:
            ticket (Ticket): Ticket issued at entry.
            payment (Payment): Payment method chosen by the driver.

        Returns:
            None

        Raises:
            RuntimeError: If the payment fails.
        """
        self.exit_gate.complete_exit(
            self.building,
            ticket,
            payment
        )
