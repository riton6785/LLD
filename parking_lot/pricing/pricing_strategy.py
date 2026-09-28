"""
===============================================================================
PricingStrategy  (Strategy Pattern)
===============================================================================

Definition
----------
Strategy is a Behavioral Design Pattern that lets us swap one algorithm
for another without changing the code that uses it.

Problem Statement
-----------------
Parking lots charge in many different ways:

    - a flat fee per visit
    - per hour
    - different rates for bikes and cars
    - weekend / night surcharges

If ExitGate computed the price itself, every pricing change would
mean editing the gate:

    if pricing_mode == "fixed":
        return 100
    elif pricing_mode == "hourly":
        return hours * 50
    ...

Solution
--------
Each pricing rule becomes its own class implementing calculate(ticket).
The rest of the system only depends on this abstract interface.

The Ticket gives a strategy everything it may need:

    ticket.get_entry_time()                    -> duration based pricing
    ticket.get_vehicle().get_vehicle_type()    -> vehicle based pricing

Benefits
--------
1. Open/Closed Principle
   New pricing = new class; ExitGate and CostComputation stay unchanged.

2. Configurable per Deployment
   Mall parking and airport parking can use the same code with
   different strategies.

Strategy Flow
-------------

ExitGate
   |
   v
CostComputation.compute(ticket)
   |
   v
PricingStrategy.calculate(ticket)   <- abstract call
   |
   v
FixedPricingStrategy                <- concrete strategy
===============================================================================
"""

from abc import ABC, abstractmethod
from ticket import Ticket


class PricingStrategy(ABC):
    """
    Abstract Strategy.

    Declares how every pricing algorithm is called.
    """

    @abstractmethod
    def calculate(self, ticket: Ticket) -> float:
        """
        Computes the parking fee for one visit.

        Args:
            ticket (Ticket): Holds vehicle, level, spot and entry time.

        Returns:
            float: Amount the driver must pay.
        """
        pass
