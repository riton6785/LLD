"""
===============================================================================
Factory Method Pattern
===============================================================================

Definition
----------
Factory Method is a Creational Design Pattern that defines an interface
for creating objects while allowing subclasses to decide which concrete
object should be instantiated.

Instead of a single factory containing all creation logic, each concrete
factory is responsible for creating a specific product.

Problem Statement
-----------------
Suppose we have multiple shape classes:

    - Circle
    - Square

In a traditional approach:

    circle = Circle()
    square = Square()

The client becomes tightly coupled to concrete product classes.

As the application grows:

1. Object creation logic becomes scattered.
2. Constructors may become complex.
3. Validation/configuration may be duplicated.
4. Product creation becomes harder to maintain.

Simple Factory Improvement
--------------------------
Simple Factory centralizes creation logic.

Example:

    shape = ShapeFactory.create_shape("circle")

However, adding a new shape requires modifying the factory.

Example:

    if shape_type == "triangle":
        return Triangle()

This violates the Open/Closed Principle.

Solution
--------
Factory Method moves creation responsibility into dedicated factory
classes.

Example:

    factory = CircleFactory()
    shape = factory.create_shape()

Each factory creates only one type of product.

Benefits
--------
1. Better Open/Closed Principle Support
   New factories can be added without modifying existing ones.

2. Eliminates Large Conditional Statements
   No large if-else chains for product creation.

3. Improved Maintainability
   Product creation logic is isolated.

4. Better Separation of Responsibilities
   Each factory manages one product.

5. Easier Extension
   New products are introduced through new factory classes.

Drawbacks
---------
1. Increased Number of Classes
   Every product usually requires a factory.

2. More Complex Structure
   Additional abstraction layers increase complexity.

3. Client Must Choose Factory
   Factory selection logic still exists somewhere.

4. Can Be Overkill
   For small applications, a Simple Factory may be sufficient.

Comparison with Simple Factory
------------------------------

Solved
------
1. Eliminates centralized product creation logic.

2. Better adherence to Open/Closed Principle.

3. Product creation logic evolves independently.

4. No large create_shape() conditional blocks.

Not Solved
----------
1. More classes are introduced.

2. Client still decides which factory to use.

3. Additional abstraction may increase complexity.

Note
----
Factory Method is an official Gang of Four (GoF) Creational Pattern.
===============================================================================
"""

from abc import ABC, abstractmethod
from shape import Circle, Square


class ShapeFactory(ABC):
    """
    Abstract Creator.

    Declares the Factory Method that concrete factories must implement.
    """

    @abstractmethod
    def create_shape(self):
        """
        Factory Method.

        Creates and returns a Shape object.

        Returns:
            Shape: Concrete shape instance.
        """
        pass


class CircleFactory(ShapeFactory):
    """
    Concrete Creator responsible for creating Circle objects.
    """

    def create_shape(self):
        """
        Creates a Circle object.

        Returns:
            Circle: Newly created Circle instance.
        """
        return Circle()


class SquareFactory(ShapeFactory):
    """
    Concrete Creator responsible for creating Square objects.
    """

    def create_shape(self):
        """
        Creates a Square object.

        Returns:
            Square: Newly created Square instance.
        """
        return Square()
