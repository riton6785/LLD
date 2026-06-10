"""
Observer implementations for the Pull-based Observer Design Pattern.

## Core Design Idea
Observers do NOT receive data directly (no push model).
Instead, they:
1. Get notified that something changed
2. Pull required data from WeatherStation

This reduces coupling between Subject and Observers.

---

## Why Pull Strategy is used here

### Problem with Push Strategy:
- Subject must know what data each observer needs
- Subject sends data even if observer does not need it
- Changes in data structure force changes in Subject

### Pull Strategy Benefits:
- Subject only notifies "something changed"
- Observers decide what to fetch
- Easier to extend without modifying WeatherStation

---

## Real-world analogy
Instead of receiving a full report every time,
observers get a notification:
👉 "Weather updated"

Then they check what they care about:
- Temperature observer → pulls temperature
- Wind observer → pulls wind

---

## Key Design Tradeoff
✔ Lower coupling between Subject and Observers  
✔ More flexible and extensible  

❌ Observers must know about Subject structure  
❌ Slight runtime dependency on Subject state availability
"""

from abc import ABC, abstractmethod


class WeatherObservers(ABC):
    """
    Abstract Observer defining contract for all weather observers.

    Each observer reacts to changes in WeatherStation state.

    In Pull Strategy:
    - No weather data is passed here
    - Observers fetch data from WeatherStation instead
    """

    @abstractmethod
    def show(self):
        pass


class TemperatureObservers(WeatherObservers):
    """
    Observer that focuses only on temperature data.

    It pulls required data from WeatherStation when notified.
    """

    def __init__(self, WeatherStation):
        self.weather_station = WeatherStation
        self.weather_station.add_observer(self)

    def show(self):
        print(
            f"Output from {self.__class__.__name__} is "
            f"{self.weather_station.weather_data.temperature_data}"
        )


class WindObservers(WeatherObservers):
    """
    Observer that focuses only on wind data.

    Demonstrates selective data pulling from subject.
    """

    def __init__(self, WeatherStation):
        self.weather_station = WeatherStation
        self.weather_station.add_observer(self)

    def show(self):
        print(
            f"Output from {self.__class__.__name__} is "
            f"{self.weather_station.weather_data.wind_data}"
        )
