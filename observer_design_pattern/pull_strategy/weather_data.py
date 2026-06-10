"""
WeatherData is a simple Value Object representing the state of the system.

## Design Intent
This class encapsulates weather-related state into a single object:
- Temperature
- Wind

Instead of passing multiple primitive values everywhere, we group them.

## Why this matters
Without this abstraction:
- WeatherStation would expose multiple scattered attributes
- Observers would depend on multiple parameters
- Any change in data structure would break multiple components

This violates encapsulation and increases maintenance cost.

## Why it fits Observer Pattern
WeatherData acts as the "state snapshot" that observers can pull from
the subject when they are notified.
"""


class WeatherData:
    def __init__(self, temperature_data, wind_data):
        self.temperature_data = temperature_data
        self.wind_data = wind_data