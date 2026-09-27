"""
===============================================================================
FixedPricingStrategy  (Concrete Strategy)
===============================================================================

Purpose
-------
The simplest pricing rule: every visit costs a flat 100, no matter
how long the vehicle stayed or what type it is.

Adding Another Strategy
-----------------------
An hourly strategy would only need a new class:

    class HourlyPricingStrategy(PricingStrategy):
        def calculate(self, ticket: Ticket) -> float:
            duration = datetime.now() - ticket.get_entry_time()
            hours = max(1, math.ceil(duration.total_seconds() / 3600))
            return hours * 50.0

and one change in client.py:

    CostComputation(HourlyPricingStrategy())

Nothing else in the system changes.
===============================================================================
"""

from .pricing_strategy import PricingStrategy
from ticket import Ticket


class FixedPricingStrategy(PricingStrategy):
    """
    Concrete Strategy.

    Charges the same flat amount for every visit.
    """

    def calculate(self, ticket: Ticket) -> float:
        """
        Args:
            ticket (Ticket): Unused here; kept to honour the interface.

        Returns:
            float: Always 100.0.
        """
        return 100.0
