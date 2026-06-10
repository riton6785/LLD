"""
Observer implementations for PUSH-based Observer Design Pattern.

## Core Idea of Push Strategy
- Subject sends full WeatherData to observers
- Observers do NOT request data
- Observers only react to incoming updates

---

## Why Push Strategy exists

Push is useful when:
- Data is small and uniform
- All observers consume same dataset
- You want simple observer logic

---

## Tradeoff vs Pull Strategy

### Push Advantages:
✔ Observers are stateless w.r.t. subject structure  
✔ Easy to implement observers  
✔ No need to hold reference to subject  

### Push Disadvantages:
❌ Subject must know what data observers need  
❌ Any change in data structure impacts all observers  
❌ Can send unnecessary data to some observers  

---

## Real-world analogy
Push = "Weather app sends full report to all widgets"

Pull = "Widgets ask weather app for only what they need"
"""

from abc import ABC, abstractmethod


class WeatherObservers(ABC):
    """
    Abstract Observer for Push Strategy.

    In Push Strategy:
    - Subject sends WeatherData directly
    - Observer receives data as input
    """

    @abstractmethod
    def show(self, weather_data):
        pass


class TemperatureObservers(WeatherObservers):
    """
    Observer interested in temperature data only.

    Even though full WeatherData is pushed,
    this observer extracts only required field.
    """

    def __init__(self):
        pass

    def show(self, weather_data):
        print(
            f"Output from {self.__class__.__name__} is "
            f"{weather_data.temperature_data}"
        )


class WindObservers(WeatherObservers):
    """
    Observer interested in wind data only.

    Receives full WeatherData but uses partial information.
    """

    def __init__(self):
        pass

    def show(self, weather_data):
        print(
            f"Output from {self.__class__.__name__} is "
            f"{weather_data.wind_data}"
        )
