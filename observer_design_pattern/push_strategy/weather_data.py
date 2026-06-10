"""
WeatherData is a Value Object representing the full state snapshot
that is PUSHED to observers.

## Design Intent
Unlike Pull Strategy, where observers fetch data,
here WeatherData is actively delivered to observers.

It acts as a transport object between Subject → Observers.

---

## Why this matters

Without this abstraction:
- Subject would need to call observer-specific methods
- Each observer would require different parameters
- Tight coupling would increase rapidly

With WeatherData:
- Subject pushes a single unified object
- Observers extract what they need from it

---

## Push Strategy implication
WeatherData defines the contract of communication:
👉 If WeatherData changes, all observers may need updates
"""

class WeatherData:
    def __init__(self, temperature_data, wind_data):
        self.temperature_data = temperature_data
        self.wind_data = wind_data
