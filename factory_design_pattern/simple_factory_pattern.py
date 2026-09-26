"""
===============================================================================
Simple Factory Pattern
===============================================================================

Definition
----------
The Simple Factory Pattern centralizes object creation logic into a single
factory class. Instead of creating objects directly throughout the application,
clients request the factory to create the required object.

Problem Statement
-----------------
Suppose we have multiple shape classes such as:

    - Circle
    - Square
    - Rectangle

These objects may be created in many places throughout the application.

Example:

    circle = Circle()
    square = Square()

Now assume that after some time the Circle creation process changes and
requires additional information, validation, configuration, or some complex
initialization logic.

Without a factory:
------------------
Every place that creates a Circle must be updated.

Problems:
1. Code duplication.
2. Tight coupling between client code and concrete classes.
3. High maintenance cost when object creation logic changes.
4. Risk of inconsistent object creation across the application.

Solution
--------
Introduce a Simple Factory that is responsible for creating shape objects.

Instead of:

    circle = Circle()

Use:

    circle = ShapeFactory.create_shape("circle")

Now all object creation logic is centralized in one place.

Benefits
--------
1. Centralized Object Creation
   Creation logic resides in a single location.

2. Reduced Code Duplication
   Clients no longer repeat creation logic.

3. Easier Maintenance
   Constructor changes are handled in the factory.

4. Better Encapsulation
   Clients do not need to know object creation details.

5. Consistent Object Creation
   Validation, logging, caching, configuration, etc. can be applied
   uniformly.

6. Reduced Coupling
   Client code depends on the factory instead of directly creating
   concrete objects.

7. Improved Readability
   Business logic remains focused on behavior rather than construction.

Drawbacks
---------
1. Violates Open/Closed Principle (OCP)

   Whenever a new shape is added, the factory must be modified.

   Example:

       if shape_type == "triangle":
           return Triangle()

2. Factory Can Become Bloated

   As the number of products increases, the factory may become large
   and difficult to maintain.

3. Tight Coupling Between Factory and Products

   The factory must know every concrete class that it can create.

4. Long Conditional Statements

   Large if-else chains can become difficult to manage.

5. Single Point of Change

   Although centralization is beneficial, all creation-related changes
   must go through the factory.

When to Use
-----------
- Small to medium number of product types.
- Object creation logic is shared across the application.
- Constructors are likely to change.
- Additional setup/validation is required during creation.

When Not to Use
---------------
- New product types are added frequently.
- Strong adherence to Open/Closed Principle is required.
- Plugin-based or highly extensible systems are being built.

Note
----
Simple Factory is not an official Gang of Four (GoF) design pattern.
GOF memebrs are Factory method pattern, Abstract Factory pattern,
It is a commonly used object creation technique and often serves as a
stepping stone toward Factory Method and Abstract Factory patterns.
===============================================================================
"""


class Circle:
    """Concrete product representing a Circle."""

    def draw_circle(self):
        return "Circle is drawn"

    def compute_area(self):
        return "Area computed"


class Square:
    """Concrete product representing a Square."""

    def draw_square(self):
        return "Square is drawn"

    def compute_area(self):
        return "Area computed"


class CreateShape:
    """
    Simple Factory responsible for creating shape objects.

    Centralizes object creation logic so that changes to object
    construction need to be made in only one place.
    """

    @staticmethod
    def create_shape(shape_type):
        """
        Creates and returns the requested shape.

        Args:
            shape_type (str): Type of shape to create.

        Returns:
            Circle | Square

        Raises:
            ValueError: If the shape type is not supported.
        """

        if shape_type == "circle":
            return Circle()

        if shape_type == "square":
            return Square()

        raise ValueError(f"Unsupported shape type: {shape_type}")


class Client:
    """
    Client code that uses the factory instead of directly
    creating concrete objects.
    """

    @staticmethod
    def main():
        square = CreateShape.create_shape("square")
        print(f"{square.draw_square()} | {square.compute_area()}")

        circle = CreateShape.create_shape("circle")
        print(f"{circle.draw_circle()} | {circle.compute_area()}")


if __name__ == "__main__":
    Client.main()
