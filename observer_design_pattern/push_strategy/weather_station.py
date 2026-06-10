"""
WeatherStation is the Subject (Observable) in Push-based Observer Pattern.

## Core Responsibility
- Maintain list of observers
- Maintain current WeatherData state
- PUSH updates to observers when state changes

---

## Why Observer Pattern is needed

Without Observer Pattern:
- WeatherStation would directly manage UI components
- Adding new display types requires modifying WeatherStation
- System becomes tightly coupled and rigid

With Observer Pattern:
- WeatherStation knows nothing about concrete observers
- New observers can be added without modifying subject logic

---

## Push Strategy Behavior

Unlike Pull Strategy:
- WeatherStation sends full WeatherData to observers
- Observers do NOT request data
- Observers are passive recipients

---

## Key Tradeoff

✔ Simple observer logic  
✔ Easy notification mechanism  

❌ Subject becomes responsible for data contract  
❌ Changes in WeatherData impact all observers  
"""

from abc import ABC, abstractmethod
from weather_observers import WeatherObservers
from weather_data import WeatherData


class Observable(ABC):
    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def set_weather_readings(self):
        pass


class WeatherStation(Observable):
    """
    Concrete Subject in Push Observer Pattern.

    Maintains:
    - List of observers
    - Current WeatherData

    Pushes updates directly to observers.
    """

    def __init__(self):
        self.observers: list[WeatherObservers] = []
        self.weather_data: WeatherData | None = None

    def add_observer(self, observer: list[WeatherObservers]):
        self.observers.extend(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.show(self.weather_data)

    def set_weather_readings(self, temperature_data, wind_data):
        self.weather_data = WeatherData(temperature_data, wind_data)
        self.notify_observers()
