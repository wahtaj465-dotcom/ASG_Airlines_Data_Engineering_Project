"""Main ETL Pipeline"""

import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]

RAW_FILE = BASE_DIR / "data/raw/UseCase - Airlines.xlsx"
BRONZE = BASE_DIR / "data/bronze"
SILVER = BASE_DIR / "data/silver"
GOLD = BASE_DIR / "data/gold"

# Create folders if they don't exist
for folder in [BRONZE, SILVER, GOLD]:
    folder.mkdir(parents=True, exist_ok=True)

print("Reading Excel file...")
excel = pd.ExcelFile(RAW_FILE)

# Read sheets
bookings = pd.read_excel(excel, "bookings")
flights = pd.read_excel(excel, "flights")
passengers = pd.read_excel(excel, "passengers")
payments = pd.read_excel(excel, "payments")

# ---------------- BRONZE ----------------
bookings.to_csv(BRONZE / "bookings.csv", index=False)
flights.to_csv(BRONZE / "flights.csv", index=False)
passengers.to_csv(BRONZE / "passengers.csv", index=False)
payments.to_csv(BRONZE / "payments.csv", index=False)

# ---------------- SILVER ----------------
bookings = bookings.drop_duplicates()
flights = flights.drop_duplicates()
passengers = passengers.drop_duplicates()
payments = payments.drop_duplicates()

bookings["booking_date"] = pd.to_datetime(bookings["booking_date"])

bookings.to_csv(SILVER / "bookings_clean.csv", index=False)
flights.to_csv(SILVER / "flights_clean.csv", index=False)
passengers.to_csv(SILVER / "passengers_clean.csv", index=False)
payments.to_csv(SILVER / "payments_clean.csv", index=False)

# ---------------- GOLD ----------------
summary = pd.DataFrame({
    "Total Bookings":[len(bookings)],
    "Total Flights":[len(flights)],
    "Passengers":[passengers["passenger_id"].nunique()],
    "Revenue":[payments["amount"].sum()]
})

summary.to_csv(GOLD / "executive_summary.csv", index=False)

print("Pipeline executed successfully.")