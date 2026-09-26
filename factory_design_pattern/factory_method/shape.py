"""
===============================================================================
Products
===============================================================================

Definition
----------
This module defines the Product hierarchy used by the Factory Method
Pattern.

The Shape class acts as an Abstract Product that defines a common
interface for all shape objects.

Concrete products implement this interface and provide shape-specific
behavior.

Products
--------
1. Circle
2. Square

Purpose
-------
Clients and factories interact through the Shape abstraction rather
than concrete implementations.

Benefits
--------
1. Supports Polymorphism
   Clients can work with Shape objects without knowing the exact type.

2. Consistent Interface
   All shapes expose the same operations.

3. Easy Extensibility
   New shapes can be introduced without affecting existing products.

4. Reduced Coupling
   Client code depends on abstractions rather than concrete classes.
===============================================================================
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Product.

    Defines the common interface that all concrete shapes must implement.
    """

    @abstractmethod
    def draw(self):
        """
        Draws the shape.

        Returns:
            str: Description of drawing operation.
        """
        pass

    @abstractmethod
    def compute_area(self):
        """
        Computes the area of the shape.

        Returns:
            str: Description of area computation.
        """
        pass


class Circle(Shape):
    """
    Concrete Product representing a Circle.
    """

    def draw(self):
        """
        Draws a Circle.

        Returns:
            str: Drawing result.
        """
        return "Circle has been drawn"

    def compute_area(self):
        """
        Computes Circle area.

        Returns:
            str: Area computation result.
        """
        return "Area computed for Circle"


class Square(Shape):
    """
    Concrete Product representing a Square.
    """

    def draw(self):
        """
        Draws a Square.

        Returns:
            str: Drawing result.
        """
        return "Square has been drawn"

    def compute_area(self):
        """
        Computes Square area.

        Returns:
            str: Area computation result.
        """
        return "Area computed for Square"
