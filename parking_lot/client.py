"""
===============================================================================
Client  (Composition Root)
===============================================================================

Purpose
-------
client.py is where the whole parking lot is ASSEMBLED and then USED.

No class in the system creates its own collaborators. Everything is
built here and passed in through constructors (Dependency Injection).
This single place is called the "composition root".

Changing behaviour is therefore a one-line change in this file:

    RandomLookupStrategy()   -> NearestLookupStrategy()
    FixedPricingStrategy()   -> HourlyPricingStrategy()
    CashPayment()            -> CardPayment()

Setup Built Below
-----------------

Level 1
   |-- Two-wheeler spots  : L1-S1, L1-S2
   |-- Four-wheeler spots : L1-S3

Level 2
   |-- Two-wheeler spots  : L2-S1
   |-- Four-wheeler spots : L2-S2, L2-S3

Workflow
--------
1. Create the spot lookup strategy.
2. Build spot managers per vehicle type, per level.
3. Build levels from managers.
4. Build the building from levels.
5. Build the ParkingLot facade with an entrance and an exit gate.
6. A bike and a car arrive -> tickets are issued.
7. Both exit: bike pays cash, car pays UPI.

Expected Output
---------------

Parking allocated at level: 1 spot: L1-S1
Parking allocated at level: 1 spot: L1-S3
Cash paid: 100.0
Exit successful. Gate opened.
UPI paid: 100.0
Exit successful. Gate opened.

How to Run
----------
From the parking_lot/ folder (the one containing this file):

    python3 client.py

Do not run files inside sub-folders directly; they are modules
meant to be imported, and their imports only resolve from here.
===============================================================================
"""

from typing import Dict

from enums.vehicle_type import VehicleType
from parking_lot.entrance_gate import EntranceGate
from parking_lot.exit_gate import ExitGate
from parking_lot.parking_building import ParkingBuilding
from parking_lot.parking_level import ParkingLevel
from parking_lot.parking_lot import ParkingLot
from parking_spot import ParkingSpot
from payment.cash_payment import CashPayment
from payment.upi_payment import UPIPayment
from pricing.cost_computation import CostComputation
from pricing.fixed_pricing_strategy import FixedPricingStrategy
from spot_lookup_strategy.parking_lookup_strategy import ParkingSpotLookupStrategy
from spot_lookup_strategy.random_lookup_strategy import RandomLookupStrategy
from spot_managers.four_wheeler_spot_manager import FourWheelerSpotManager
from spot_managers.parking_spot_manager import ParkingSpotManager
from spot_managers.two_wheeler_spot_manager import TwoWheelerSpotManager
from vehicle import Vehicle

class ParkingLotClient:
    """
    Demonstrates building and using the parking lot system.
    """

    @staticmethod
    def main():
        """
        Application entry point.

        Wires every object together, then simulates two vehicles
        arriving and leaving.

        Returns:
            None
        """

        # Lookup strategy (shared by all managers; it holds no state)
        strategy: ParkingSpotLookupStrategy = RandomLookupStrategy()

        # -----------------------------
        # Level 1
        # One manager per vehicle type; each owns its own spots.
        # -----------------------------
        level_one_managers: Dict[VehicleType, ParkingSpotManager] = {}

        level_one_managers[VehicleType.TWO_WHEELER] = (
            TwoWheelerSpotManager(
                [
                    ParkingSpot("L1-S1"),
                    ParkingSpot("L1-S2")
                ],
                strategy
            )
        )

        level_one_managers[VehicleType.FOUR_WHEELER] = (
            FourWheelerSpotManager(
                [
                    ParkingSpot("L1-S3")
                ],
                strategy
            )
        )

        level1 = ParkingLevel(
            1,
            level_one_managers
        )

        # -----------------------------
        # Level 2
        # -----------------------------
        level_two_managers: Dict[VehicleType, ParkingSpotManager] = {}

        level_two_managers[VehicleType.TWO_WHEELER] = (
            TwoWheelerSpotManager(
                [
                    ParkingSpot("L2-S1")
                ],
                strategy
            )
        )

        level_two_managers[VehicleType.FOUR_WHEELER] = (
            FourWheelerSpotManager(
                [
                    ParkingSpot("L2-S2"),
                    ParkingSpot("L2-S3")
                ],
                strategy
            )
        )

        level2 = ParkingLevel(
            2,
            level_two_managers
        )

        # -----------------------------
        # Parking Building
        # Levels are tried in this order when allocating.
        # -----------------------------
        parking_building = ParkingBuilding([level1, level2])

        # -----------------------------
        # Parking Lot (Facade)
        # Pricing is injected into the exit gate.
        # -----------------------------
        parking_lot = ParkingLot(
            parking_building,
            EntranceGate(),
            ExitGate(
                CostComputation(
                    FixedPricingStrategy()
                )
            )
        )

        # -----------------------------
        # Vehicles
        # -----------------------------
        bike = Vehicle(
            "BIKE-101",
            VehicleType.TWO_WHEELER
        )

        car = Vehicle(
            "CAR-201",
            VehicleType.FOUR_WHEELER
        )

        # -----------------------------
        # Vehicle Arrivals
        # Bike -> first free two-wheeler spot (L1-S1)
        # Car  -> first free four-wheeler spot (L1-S3)
        # -----------------------------
        t1 = parking_lot.vehicle_arrives(bike)
        t2 = parking_lot.vehicle_arrives(car)

        # -----------------------------
        # Vehicle Exits
        # Payment method is chosen per exit (Strategy at runtime).
        # -----------------------------
        parking_lot.vehicle_exits(
            t1,
            CashPayment()
        )

        parking_lot.vehicle_exits(
            t2,
            UPIPayment()
        )


if __name__ == "__main__":
    ParkingLotClient.main()
