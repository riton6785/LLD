class Vehicle:
    """
    PROBLEM DESIGN:

    This base class defines a default driving behavior.
    Subclasses override this method to change behavior.
    """

    def drive(self):
        # ❌ Problem: Behavior is fixed inside class hierarchy
        # If we want different driving logic, we must create new subclasses
        print(f"\n{self.__class__.__name__}:")
        print("Driving Capability: Normal")


class SuperCars(Vehicle):
    """
    ❌ PROBLEM 1: Code duplication risk

    'Sports driving' logic is repeated in multiple classes.
    If logic changes → we must update in many places.
    """

    def drive(self):
        print(f"\n{self.__class__.__name__}:")
        print("Driving Capability: Sports")


class NormalVehicle(Vehicle):
    """
    ❌ PROBLEM 2: Rigid design

    Behavior is locked inside class.
    Cannot change driving behavior dynamically.
    """

    def drive(self):
        print(f"\n{self.__class__.__name__}:")
        print("Driving Capability: Normal")


class GoodsVehicle(Vehicle):
    """
    ❌ PROBLEM 3: Class explosion risk

    Every new behavior combination = new class.
    System becomes hard to maintain as it grows.
    """

    def drive(self):
        print(f"\n{self.__class__.__name__}:")
        print("Driving Capability: Sports")


"""
❌ SUMMARY OF PROBLEMS:

1. Code duplication (same logic repeated)
2. Behavior tightly coupled with class
3. No runtime flexibility
4. Class explosion with new features
"""
