"""
===============================================================================
UPIPayment  (Concrete Strategy)
===============================================================================

Purpose
-------
Payment through UPI (scan-and-pay).

In this teaching example the payment always succeeds. A real
implementation would call a payment gateway and return False when
the transaction is declined or times out.
===============================================================================
"""

from .payment import Payment


class UPIPayment(Payment):
    """
    Concrete Strategy.

    Collects the fee through UPI.
    """

    def pay(self, amount: float) -> bool:
        """
        Args:
            amount (float): Fee to collect.

        Returns:
            bool: Always True in this example.
        """
        print(f"UPI paid: {amount}")
        return True
