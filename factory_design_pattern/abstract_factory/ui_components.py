"""
===============================================================================
Products
===============================================================================

This module defines product families used by the Abstract Factory Pattern.

Product Family 1:
    Button

Product Family 2:
    Checkbox

Concrete Variants:
    LightButton
    DarkButton

    LightCheckbox
    DarkCheckbox
===============================================================================
"""

from abc import ABC, abstractmethod


# ----------------------
# Abstract Products
# ----------------------

class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def render(self):
        pass


# ----------------------
# Light Theme Products
# ----------------------

class LightButton(Button):

    def render(self):
        return "Rendering Light Button"


class LightCheckbox(Checkbox):

    def render(self):
        return "Rendering Light Checkbox"


# ----------------------
# Dark Theme Products
# ----------------------

class DarkButton(Button):

    def render(self):
        return "Rendering Dark Button"


class DarkCheckbox(Checkbox):

    def render(self):
        return "Rendering Dark Checkbox"
