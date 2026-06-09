from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    """
    STRATEGY PATTERN IDEA:

    We separate "what changes often" (behavior)
    from "what stays stable" (Vehicle class).

    Instead of inheritance, we use composition.
    """

    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):
    """
    ✔ Encapsulated reusable behavior

    This logic is written ONCE and reused everywhere.
    """

    def drive(self):
        return "Driving Capability: Normal"


class SportsDriveStrategy(DriveStrategy):
    """
    ✔ Another independent behavior

    Can be used by any vehicle at runtime.
    """

    def drive(self):
        return "Driving Capability: Sports"


class Vehicle:
    """
    ✔ SOLUTION DESIGN:

    Vehicle does NOT decide how it drives.

    It delegates driving behavior to a strategy object.
    """

    def __init__(self, drive_strategy: DriveStrategy):
        # ✔ Behavior is injected (NOT hardcoded)
        self.drive_strategy = drive_strategy

    def drive(self):
        """
        ✔ Delegation:

        Vehicle does NOT implement logic itself.
        It asks strategy to perform behavior.
        """
        print(f"\n{self.__class__.__name__}:")
        print(self.drive_strategy.drive())


"""
✔ BENEFITS OF THIS DESIGN:

1. No duplication → behavior written once
2. No class explosion → no need for subclasses
3. Behavior is swappable at runtime
4. Follows "composition over inheritance"
5. Open/Closed Principle (OCP) is satisfied
"""
