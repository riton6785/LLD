"""
Problem Statement
-----------------

Suppose we have a pizza shop that offers a base pizza such as Margerita
and allows customers to add toppings like cheese, vegetables, mushrooms,
olives, etc.

A naive inheritance-based design would create a separate class for every
possible combination:

    Margerita
    CheeseMargerita
    VeggieMargerita
    CheeseVeggieMargerita
    CheeseVeggieOliveMargerita
    ...

As the number of toppings increases, the number of classes grows rapidly,
resulting in a problem known as 'Class Explosion'.

Issues with this approach:
1. Every new topping combination requires a new class.
2. Significant code duplication across classes.
3. Difficult to maintain and extend.
4. Violates the Open/Closed Principle because new combinations require
   creating additional subclasses.
5. Customizations cannot be composed dynamically at runtime.
6. The design becomes increasingly difficult to understand as the
   product catalog grows.

This problem is a classic motivation for using the Decorator Pattern,
where toppings are added dynamically by wrapping an existing pizza object
instead of creating a new subclass for every combination.
"""

from abc import ABC, abstractmethod


class BasePizza(ABC):
    """
    Abstract base class representing a pizza.

    Every pizza implementation must provide:
    - name
    - cost
    - description

    This serves as the common contract for all pizza types.
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
    Concrete implementation of a basic Margerita pizza.

    In a traditional inheritance-based design, every topping variation
    would inherit from this class and override behavior as needed.
    """

    def get_name(self):
        return f"Pizza of type {self.__class__.__name__}"

    def get_cost(self):
        return 200

    def get_description(self):
        return "Classic Margerita Pizza"


class CheeseMargerita(Margerita):
    """
    Represents a Margerita pizza with cheese.

    Problem:
    --------
    If we continue this approach, we would also need classes such as:

        VeggieMargerita
        MushroomMargerita
        CheeseVeggieMargerita
        CheeseVeggieMushroomMargerita
        OliveCheeseVeggieMargerita

    and so on...

    Each new combination requires another subclass, leading to
    class explosion and increased maintenance costs.
    """

    def get_name(self):
        return f"Pizza of type {self.__class__.__name__}"

    def get_cost(self):
        return 250

    def get_description(self):
        return "Margerita Pizza with Extra Cheese"
