"""
Decorator Pattern - Pizza Shop Example
======================================

Problem Statement
-----------------

A pizza shop offers multiple base pizzas such as:

    - Margerita
    - Farmhouse

Customers can then customize these pizzas by adding toppings such as:

    - Cheese
    - Mushrooms
    - Vegetables
    - Olives
    - Paneer
    - Corn

In the inheritance-based solution, every topping combination would require
a new subclass.

Examples:

    CheeseMargerita
    VeggieMargerita
    MushroomMargerita
    CheeseVeggieMargerita
    CheeseVeggieMushroomMargerita

As more toppings are introduced, the number of classes grows exponentially,
making the system difficult to maintain.

Decorator Pattern Solution
--------------------------

Instead of creating a subclass for every combination, we separate the concept
of:

    1. Base Pizza
    2. Additional Toppings

A pizza starts as a simple object:

    Margerita()

and toppings are added dynamically by wrapping the pizza object:

    CheeseTopping(
        VeggiesTopping(
            MushroomTopping(
                Margerita()
            )
        )
    )

Benefits
--------

1. Avoids class explosion.
2. New toppings can be added without modifying existing code.
3. Supports runtime customization.
4. Follows the Open/Closed Principle.
5. Keeps the design flexible and maintainable.

This file contains the core pizza abstractions and concrete pizza types.
"""

from abc import ABC, abstractmethod


class BasePizza(ABC):
    """
    Common contract for every pizza in the system.

    Why do we need this?
    --------------------

    Decorators and concrete pizzas must behave uniformly.

    Whether the object is:

        Margerita()

    or

        CheeseTopping(
            MushroomTopping(
                Margerita()
            )
        )

    the client should be able to interact with it using the same interface.

    This abstraction enables decorators to wrap pizzas transparently.
    """

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class Margerita(BasePizza):
    """
    Concrete Pizza Implementation.

    Represents a plain Margerita pizza without any toppings.

    This serves as a base object that can later be decorated with
    additional toppings.

    Example:

        Margerita()

    Cost:

        200
    """

    def get_name(self):
        return f"Pizza of type {self.__class__.__name__}"

    def get_cost(self):
        return 200

    def get_description(self):
        print(self.get_name() + " And price is: " + str(self.get_cost()))


class Farmhouse(BasePizza):
    """
    Another concrete pizza implementation.

    Represents a Farmhouse pizza before any customization.

    Just like Margerita, this object can be wrapped by one or more
    decorators to dynamically add toppings.

    Example:

        CheeseTopping(
            VeggiesTopping(
                Farmhouse()
            )
        )
    """

    def get_name(self):
        return f"Pizza of type {self.__class__.__name__}"

    def get_cost(self):
        return 220

    def get_description(self):
        print(self.get_name() + " And price is: " + str(self.get_cost()))
