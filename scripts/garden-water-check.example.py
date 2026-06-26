#!/usr/bin/env python3
"""
Example: Garden Water Check — automated weather monitoring script.
This demonstrates API integration, cron scheduling, JSON processing, 
and environment-variable-based configuration.

Full version kept private; this is a representative sample.
"""

import json
import os
import urllib.request
from datetime import date

# ── Secrets loaded from environment (never hardcoded) ──
TEMPEST_TOKEN = os.environ.get("TEMPEST_API_TOKEN", "env:TEMPEST_API_TOKEN")
STATION_ID = int(os.environ.get("TEMPEST_STATION_ID"))
TODAY = date.today()


def fetch_weather():
    """
    Fetch current conditions + forecast from WeatherFlow Tempest API.
    Demonstrates: REST API call, token auth, JSON parsing, unit conversion.
    """
    url = (
        f"https://swd.weatherflow.com/swd/rest/better_forecast"
        f"?station_id={STATION_ID}"
        f"&token={TEMPEST_TOKEN}"
        f"&units_temp=f&units_wind=mph&units_precip=in"
        f"&units_distance=mi"
    )
    
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read())
    
    return data.get("current_conditions", {}), data.get("forecast", {})


def evaluate_plants(cc, daily):
    """
    Evaluate watering needs based on:
    - Lifecycle stage (new → establishing → young → mature)
    - Days since last water
    - Weather adjustments (rain, heat, wind, humidity)
    - Per-tree sun exposure and water needs profiles
    """
    # Key logic: base intervals adjusted by weather deltas
    results = []
    
    # ... tree-specific evaluation logic ...
    # (Full version: 21 Japanese maples, CSV-driven, with rain journal)
    
    return results


def post_to_discord(report, channel):
    """
    Post formatted report via Discord webhook / bot API.
    Demonstrates: platform integration, markdown formatting, conditional output.
    """
    # ... Discord message construction and sending ...
    pass


def main():
    print(f"🌤  Garden Water Check — {TODAY}")
    print("ℹ️  Fetching weather data from Tempest API...")
    
    cc, forecast = fetch_weather()
    temp = cc.get("air_temperature", "?")
    conditions = cc.get("conditions", "?")
    
    print(f"📍 Station {STATION_ID}")
    print(f"🌡️  {conditions} · {temp}°F")
    print(f"💧 Processing tree water requirements...")
    
    results = evaluate_plants(cc, forecast.get("daily", []))
    print(f"✅ Check complete.")


if __name__ == "__main__":
    main()
