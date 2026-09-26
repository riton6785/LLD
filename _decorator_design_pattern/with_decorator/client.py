"""
Client Code
===========

Purpose
-------

The client demonstrates how pizzas can be customized dynamically
at runtime using decorators.

Without Decorator Pattern
-------------------------

We would need classes like:

    CheeseMargerita
    VeggieMargerita
    CheeseVeggieMargerita
    CheeseVeggieMushroomMargerita

Every new topping combination would require a new subclass.

With Decorator Pattern
----------------------

We start with a base pizza:

    Margerita()

and progressively wrap it with decorators:

    MushroomTopping
        ↓
    VeggiesTopping
        ↓
    CheeseTopping

This produces the same result while avoiding class explosion.

Runtime Composition Example
---------------------------

    CheeseTopping(
        VeggiesTopping(
            MushroomTopping(
                Margerita()
            )
        )
    )

Final Cost Calculation:

    Margerita      = 200
    Mushroom       = 30
    Veggies        = 40
    Cheese         = 50
    -------------------
    Total          = 320

Notice that no special subclass was required to represent this
combination.
"""

from base_pizzas import Margerita, Farmhouse
from topping_decorator import (
    VeggiesTopping,
    CheeseTopping,
    MushroomTopping,
)


class Client:
    """
    Demonstrates usage of the Decorator Pattern.

    The client does not care whether it is working with:

        - A plain pizza
        - A decorated pizza

    Because every object follows the BasePizza interface.
    """

    @staticmethod
    def main():

        # Plain Margerita
        base_pizza = Margerita()
        base_pizza.get_description()

        # Margerita with vegetables
        veggies_topping = VeggiesTopping(base_pizza)
        veggies_topping.get_description()

        # Fully customized pizza
        mixup_margerita = CheeseTopping(
            VeggiesTopping(
                MushroomTopping(
                    Margerita()
                )
            )
        )

        mixup_margerita.get_description()


if __name__ == "__main__":
    Client.main()
