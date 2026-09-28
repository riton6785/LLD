"""
===============================================================================
CashPayment  (Concrete Strategy)
===============================================================================

Purpose
-------
Payment by cash at the exit booth.

In this teaching example the payment always succeeds. A real system
might record the cash drawer transaction or compute change to return.
===============================================================================
"""

from .payment import Payment


class CashPayment(Payment):
    """
    Concrete Strategy.

    Collects the fee in cash.
    """

    def pay(self, amount: float) -> bool:
        """
        Args:
            amount (float): Fee to collect.

        Returns:
            bool: Always True in this example.
        """
        print(f"Cash paid: {amount}")
        return True
