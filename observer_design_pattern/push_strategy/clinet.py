"""
Client entry point for the Push-based Observer Design Pattern.

## Design Intent
The client is responsible for:
- Creating the WeatherStation (Subject)
- Creating observer instances
- Registering observers in bulk
- Triggering state changes

This keeps object wiring external to business logic.

---

## Why Push Strategy is used here

In Push Strategy:
- WeatherStation actively sends data to observers
- Observers do NOT fetch data themselves

This is useful when:
- All observers need same data format
- You want immediate propagation of full state
- Simpler observer logic is preferred

---

## Key Design Difference from Pull Strategy

Instead of:
👉 Observers asking for data

We do:
👉 Subject pushing data to observers

This shifts responsibility from observer → subject.

---

## Tradeoff
✔ Simple observer implementation  
✔ No dependency on subject structure inside observer  

❌ Subject becomes tightly coupled to data structure  
❌ Harder to evolve data format without modifying subject or observers  
"""

from weather_station import WeatherStation
from weather_observers import TemperatureObservers, WindObservers


class Client:
    @staticmethod
    def run():
        weather_station = WeatherStation()

        # Observers are created independently
        temperature_observer = TemperatureObservers()
        wind_observer = WindObservers()

        # Batch registration (push-style setup)
        weather_station.add_observer([temperature_observer, wind_observer])

        # State change triggers push notification
        weather_station.set_weather_readings(45, "High speed")


if __name__ == "__main__":
    Client.run()
