"""Data Validation Functions"""

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SILVER = BASE_DIR / "data/silver"

bookings = pd.read_csv(SILVER / "bookings_clean.csv")
flights = pd.read_csv(SILVER / "flights_clean.csv")
passengers = pd.read_csv(SILVER / "passengers_clean.csv")

print("========== DATA VALIDATION ==========")

# Duplicate bookings
dup_booking = bookings["booking_id"].duplicated().sum()
print(f"Duplicate Booking IDs : {dup_booking}")

# Duplicate flights
dup_flight = flights["flight_id"].duplicated().sum()
print(f"Duplicate Flight IDs  : {dup_flight}")

# Missing passengers
missing_pass = passengers["passenger_id"].isnull().sum()
print(f"Missing Passenger IDs : {missing_pass}")

# Invalid age
invalid_age = ((passengers["age"] < 0) | (passengers["age"] > 100)).sum()
print(f"Invalid Ages          : {invalid_age}")

if dup_booking == 0 and dup_flight == 0 and missing_pass == 0:
    print("\nValidation PASSED")
else:
    print("\nValidation FAILED")