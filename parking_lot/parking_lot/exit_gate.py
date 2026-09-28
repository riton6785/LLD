"""
===============================================================================
ExitGate
===============================================================================

Purpose
-------
The ExitGate models the barrier where vehicles leave. It runs the
checkout process in a strict order:

1. Compute the price       -> CostComputation (pricing strategy)
2. Collect the payment     -> Payment (payment strategy)
3. Free the spot           -> ParkingBuilding.release(ticket)
4. Open the gate

Why This Order Matters
----------------------
The spot is released only AFTER the payment succeeds.

If we released first and the payment then failed, the spot would be
marked FREE while the car is still standing in it, and the next car
could be sent to an occupied spot. Releasing last prevents that.

If payment fails, a RuntimeError is raised, the spot stays OCCUPIED
and the gate stays closed.

Two Strategies Meet Here
------------------------
1. Pricing strategy is fixed per gate (injected in the constructor).
2. Payment strategy is chosen per exit (passed to complete_exit).

Flow
----

ParkingLot.vehicle_exits(ticket, payment)
   |
   v
ExitGate.complete_exit(building, ticket, payment)
   |
   |-- calculate_price(ticket) --> CostComputation --> PricingStrategy
   |
   |-- payment.pay(amount)     --> CashPayment / UPIPayment
   |
   |-- building.release(ticket)
   |
   v
"Exit successful. Gate opened."
===============================================================================
"""

from ticket import Ticket
from .parking_building import ParkingBuilding
from payment.payment import Payment
from pricing.cost_computation import CostComputation


class ExitGate:
    """
    Checkout point for vehicles: price, pay, release.
    """

    def __init__(self, cost_computation: CostComputation):
        """
        Args:
            cost_computation (CostComputation): Pricing context used to
                compute the fee of every exiting vehicle.
        """
        self.cost_computation = cost_computation

    def complete_exit(
        self,
        building: ParkingBuilding,
        ticket: Ticket,
        payment: Payment
    ) -> None:
        """
        Runs the full checkout for one vehicle.

        Args:
            building (ParkingBuilding): Building that owns the spot.
            ticket (Ticket): Ticket issued at entry.
            payment (Payment): Payment method chosen by the driver.

        Returns:
            None

        Raises:
            RuntimeError: If the payment fails; the spot stays occupied.
        """

        amount = self.calculate_price(ticket)

        success = payment.pay(amount)

        if not success:
            raise RuntimeError("Payment failed. Exit denied.")

        # Release only after successful payment (see module docstring).
        building.release(ticket)

        print("Exit successful. Gate opened.")

    def calculate_price(self, ticket: Ticket) -> float:
        """
        Delegates fee calculation to the pricing context.

        Args:
            ticket (Ticket): Ticket being paid for.

        Returns:
            float: Amount due.
        """
        return self.cost_computation.compute(ticket)
