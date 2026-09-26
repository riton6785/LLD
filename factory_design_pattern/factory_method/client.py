"""
===============================================================================
Client
===============================================================================

Purpose
-------
Demonstrates how client code interacts with factories rather than
directly creating product objects.

The client chooses a concrete factory and delegates object creation
to the factory.

Workflow
--------
1. Create CircleFactory.
2. Request Circle creation.
3. Create SquareFactory.
4. Request Square creation.

Benefits
--------
1. Client is decoupled from object creation details.

2. Product construction logic remains inside factories.

3. Business logic focuses on behavior rather than construction.

4. Easier maintenance when creation logic changes.

Factory Method Flow
-------------------

Client
   |
   v
Concrete Factory
   |
   v
Factory Method
   |
   v
Concrete Product
===============================================================================
"""

from shape_factory import CircleFactory, SquareFactory


class Client:
    """
    Demonstrates Factory Method Pattern usage.

    The client does not instantiate concrete products directly.
    Instead, it delegates object creation to factories.
    """

    @staticmethod
    def main():
        """
        Application entry point.

        Creates factories, generates shape objects,
        and invokes shape operations.

        Returns:
            None
        """

        circle_factory = CircleFactory()
        circle = circle_factory.create_shape()

        print(
            f"{circle.draw()} | {circle.compute_area()}"
        )

        square_factory = SquareFactory()
        square = square_factory.create_shape()

        print(
            f"{square.draw()} | {square.compute_area()}"
        )


if __name__ == "__main__":
    Client.main()
