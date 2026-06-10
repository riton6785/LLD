"""
WeatherStation implements the Subject (Observable) in the Observer Pattern.

## Core Responsibility
- Maintain list of observers
- Store current weather state
- Notify observers when state changes

---

## Why Observer Pattern is needed here

Without Observer Pattern:
- WeatherStation would need to directly call each display component
- Adding new display types would require modifying WeatherStation
- Tight coupling would make system rigid and hard to extend

With Observer Pattern:
- WeatherStation is unaware of concrete observers
- New observers can be added without modifying WeatherStation

---

## Pull Strategy Behavior

WeatherStation does NOT send data to observers.

Instead:
- It only signals: "state changed"
- Observers pull required data when needed

This reduces coupling but shifts responsibility to observers.

---

## Tradeoff
✔ Open for extension (new observers easily added)  
✔ Subject remains simple and stable  

❌ Observers depend on subject state structure  
"""

from abc import ABC, abstractmethod
from weather_data import WeatherData


class WeatherObservable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass

    @abstractmethod
    def set_weather_data(self, temperature_data, wind_data):
        pass


class WeatherStation(WeatherObservable):
    """
    Concrete Subject in Observer Pattern.

    Maintains:
    - List of observers
    - Current WeatherData state

    When state changes, all observers are notified.
    """

    def __init__(self):
        self.observers = []
        self.weather_data: WeatherData | None = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.show()

    def set_weather_data(self, temperature_data, wind_data):
        self.weather_data = WeatherData(temperature_data, wind_data)
        self.notify_observer()
