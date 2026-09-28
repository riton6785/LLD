"""
===============================================================================
CostComputation  (Strategy Context)
===============================================================================

Purpose
-------
CostComputation is the Context of the pricing Strategy Pattern.

It holds a PricingStrategy and exposes one method, compute(ticket),
that the ExitGate calls. The gate never talks to a pricing strategy
directly.

Why Not Let ExitGate Hold the Strategy Directly?
------------------------------------------------
It could, and the design would still work. Having a dedicated context
gives one place to add cross-cutting pricing rules that apply to EVERY
strategy, for example:

    - adding GST / tax on top of the base price
    - applying a discount coupon
    - rounding to the nearest rupee

    def compute(self, ticket):
        base = self.pricing_strategy.calculate(ticket)
        return round(base * 1.18, 2)        # +18% tax

The gate stays unaware of these details.

Flow
----

ExitGate.calculate_price(ticket)
   |
   v
CostComputation.compute(ticket)
   |
   v
PricingStrategy.calculate(ticket)
===============================================================================
"""

from ticket import Ticket
from .pricing_strategy import PricingStrategy


class CostComputation:
    """
    Strategy Context for pricing.

    Delegates the fee calculation to the injected PricingStrategy.
    """

    def __init__(self, pricing_strategy: PricingStrategy):
        """
        Args:
            pricing_strategy (PricingStrategy): Algorithm used to price
                a visit.
        """
        self.pricing_strategy = pricing_strategy

    def compute(self, ticket: Ticket) -> float:
        """
        Computes the amount due for a ticket.

        Args:
            ticket (Ticket): The ticket being paid for at exit.

        Returns:
            float: Amount the driver must pay.
        """
        return self.pricing_strategy.calculate(ticket)
