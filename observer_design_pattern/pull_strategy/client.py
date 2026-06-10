"""
Client entry point for the Pull-based Observer Design Pattern implementation.

## Design Intent
The client is responsible for wiring the system together:
- It creates a single WeatherStation (Subject)
- It registers multiple observers (Temperature, Wind)
- It triggers state changes in the WeatherStation

This ensures that the client controls object composition, not the objects themselves.

## Pull Strategy Insight
Observers do NOT receive data directly.
Instead, they "pull" required data from the WeatherStation when notified.

This avoids:
- Tight coupling of subject → observer data format
- Sending unnecessary data to observers

Instead, observers decide what they need at runtime.
"""

from weather_station import WeatherStation
from weather_observers import TemperatureObservers, WindObservers


class Client:
    @staticmethod
    def run():
        # Single shared subject instance
        weather_station = WeatherStation()

        # Observers register themselves with the subject
        TemperatureObservers(weather_station)
        WindObservers(weather_station)

        # State change triggers notification
        weather_station.set_weather_data(45, "High speed")


if __name__ == "__main__":
    Client.run()