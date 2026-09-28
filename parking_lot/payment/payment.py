"""
===============================================================================
Payment  (Strategy Pattern)
===============================================================================

Definition
----------
Payment is an abstract interface for "how the driver pays".
Each payment method is a concrete strategy chosen at exit time.

Problem Statement
-----------------
Drivers may pay by cash, UPI, card, wallet, FASTag ...

Without an abstraction, ExitGate would contain:

    if method == "cash":
        ...
    elif method == "upi":
        ...
    elif method == "card":
        ...

and would need editing for every new payment method.

Solution
--------
ExitGate only depends on this interface:

    success = payment.pay(amount)

The driver (client) chooses the concrete method per exit:

    parking_lot.vehicle_exits(ticket, CashPayment())
    parking_lot.vehicle_exits(ticket, UPIPayment())

Contract
--------
pay(amount) must return:

    True   -> money received, gate may open
    False  -> payment failed, ExitGate refuses the exit

Benefits
--------
1. Open/Closed Principle
   CardPayment can be added without touching ExitGate.

2. Runtime Choice
   The payment method is chosen per exit, not fixed per gate.

3. Testability
   A fake payment returning False easily tests the failure path.
===============================================================================
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Abstract Strategy.

    Declares the single operation every payment method must implement.
    """

    @abstractmethod
    def pay(self, amount: float) -> bool:
        """
        Collects the given amount from the driver.

        Args:
            amount (float): Fee computed by CostComputation.

        Returns:
            bool: True if payment succeeded, False otherwise.
        """
        pass
