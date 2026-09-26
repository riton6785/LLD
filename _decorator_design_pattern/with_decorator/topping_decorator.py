"""
Decorator Implementations
=========================

Why Decorators?
---------------

Suppose a customer orders:

    Margerita + Mushroom + Veggies + Cheese

With inheritance, we might need:

    CheeseVeggiesMushroomMargerita

Now imagine adding:

    Olive
    Paneer
    Corn
    Jalapeno

The number of possible combinations becomes enormous.

Instead of creating new subclasses, the Decorator Pattern allows us
to add behavior dynamically.

The idea is simple:

    Base Pizza
        ↓
    Wrap with Mushroom
        ↓
    Wrap with Veggies
        ↓
    Wrap with Cheese

Every decorator:

    - Adds its own cost.
    - Adds its own description.
    - Delegates existing behavior to the wrapped pizza.

This creates a chain of enhancements without changing the original object.
"""

from base_pizzas import BasePizza


class ToppingDecorator(BasePizza):
    """
    Base Decorator Class.

    Purpose
    -------

    Holds a reference to another pizza object and forwards calls to it.

    Every topping decorator inherits from this class.

    Example:

        Margerita()
            ↓
        MushroomTopping()
            ↓
        CheeseTopping()

    Each layer wraps the previous layer and enhances its behavior.
    """

    def __init__(self, base_pizza: BasePizza):
        self.base_pizza = base_pizza

    def get_name(self):
        return self.base_pizza.get_name()

    def get_cost(self):
        return self.base_pizza.get_cost()

    def get_description(self):
        return self.base_pizza.get_description()


class MushroomTopping(ToppingDecorator):
    """
    Concrete Decorator.

    Adds mushroom topping to an existing pizza.

    Responsibilities:
    -----------------
    1. Increase pizza cost.
    2. Extend pizza description.
    3. Preserve existing pizza behavior.

    Example:

        MushroomTopping(
            Margerita()
        )

    Result:

        Margerita + Mushroom
    """

    def __init__(self, base_pizza: BasePizza):
        super().__init__(base_pizza)

    def get_name(self):
        return self.base_pizza.get_name() + ", Mushroom Topping"

    def get_cost(self):
        return self.base_pizza.get_cost() + 30

    def get_description(self):
        print(self.get_name() + " And price is: " + str(self.get_cost()))


class VeggiesTopping(ToppingDecorator):
    """
    Concrete Decorator.

    Adds vegetables to an existing pizza.

    Example:

        VeggiesTopping(
            MushroomTopping(
                Margerita()
            )
        )

    Result:

        Margerita + Mushroom + Veggies
    """

    def __init__(self, base_pizza: BasePizza):
        super().__init__(base_pizza)

    def get_name(self):
        return self.base_pizza.get_name() + ", Veggies Topping"

    def get_cost(self):
        return self.base_pizza.get_cost() + 40

    def get_description(self):
        print(self.get_name() + " And price is: " + str(self.get_cost()))


class CheeseTopping(ToppingDecorator):
    """
    Concrete Decorator.

    Adds cheese topping to an existing pizza.

    This decorator can wrap either:

        - A plain pizza
        - Another decorator

    Example:

        CheeseTopping(
            VeggiesTopping(
                MushroomTopping(
                    Margerita()
                )
            )
        )

    Result:

        Margerita + Mushroom + Veggies + Cheese
    """

    def __init__(self, base_pizza: BasePizza):
        super().__init__(base_pizza)

    def get_name(self):
        return self.base_pizza.get_name() + ", Cheese Topping"

    def get_cost(self):
        return self.base_pizza.get_cost() + 50

    def get_description(self):
        print(self.get_name() + " And price is: " + str(self.get_cost()))
