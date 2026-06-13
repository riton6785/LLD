"""
===============================================================================
Abstract Factory Pattern
===============================================================================

Definition
----------
Provides an interface for creating families of related objects without
specifying their concrete classes.

Abstract Factory
    =
    Multiple Factory Methods
    +
    Family Consistency

In this example:

Theme Factory creates:

    1. Button
    2. Checkbox

LightThemeFactory creates:

    LightButton
    LightCheckbox

DarkThemeFactory creates:

    DarkButton
    DarkCheckbox

Benefits
--------
1. Ensures consistency among related objects.
2. Encapsulates creation logic.
3. Supports entire product families.
4. Easy to switch product families.

Drawbacks
---------
1. Many classes.
2. Difficult to add new product types.
===============================================================================
"""

from abc import ABC, abstractmethod

from ui_components import (
    LightButton,
    LightCheckbox,
    DarkButton,
    DarkCheckbox,
)


class ThemeFactory(ABC):
    """
    Abstract Factory.

    Declares methods for creating all products
    belonging to a family.
    """

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class LightThemeFactory(ThemeFactory):
    """
    Creates Light Theme components.
    """

    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()


class DarkThemeFactory(ThemeFactory):
    """
    Creates Dark Theme components.
    """

    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()
