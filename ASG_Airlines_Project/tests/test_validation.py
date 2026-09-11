import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SILVER = BASE_DIR / "data/silver"

bookings = pd.read_csv(SILVER / "bookings_clean.csv")
flights = pd.read_csv(SILVER / "flights_clean.csv")

def test_booking_duplicates():
    assert bookings["booking_id"].duplicated().sum() == 0

def test_flight_duplicates():
    assert flights["flight_id"].duplicated().sum() == 0

print("All validation tests passed.")