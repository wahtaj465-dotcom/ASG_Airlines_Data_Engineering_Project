import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB = BASE_DIR / "sql/airlines.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

def test_total_bookings():
    cursor.execute("SELECT COUNT(*) FROM bookings")
    result = cursor.fetchone()[0]
    assert result > 0

def test_total_revenue():
    cursor.execute("SELECT SUM(amount) FROM payments")
    result = cursor.fetchone()[0]
    assert result > 0

test_total_bookings()
test_total_revenue()

print("SQL tests passed successfully.")
conn.close()