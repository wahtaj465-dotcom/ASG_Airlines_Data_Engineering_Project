-- ==========================================
-- ASG AIRLINES DATA WAREHOUSE
-- Dimension Tables
-- ==========================================

CREATE TABLE dim_flights (
    flight_key INTEGER PRIMARY KEY,
    flight_id TEXT,
    airline TEXT,
    source TEXT,
    destination TEXT,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    duration_minutes INTEGER,
    is_overnight BOOLEAN
);

CREATE TABLE dim_passengers (
    passenger_key INTEGER PRIMARY KEY,
    passenger_id TEXT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    gender TEXT,
    date_of_birth DATE,
    aadhaar_hash TEXT,
    email_hash TEXT,
    phone_masked TEXT
);

-- ==========================================
-- Fact Tables
-- ==========================================

CREATE TABLE fact_bookings (
    booking_id TEXT PRIMARY KEY,
    passenger_key INTEGER,
    flight_key INTEGER,
    booking_date TIMESTAMP,
    status TEXT,
    seat_number TEXT
);

CREATE TABLE fact_payments (
    payment_id TEXT PRIMARY KEY,
    booking_id TEXT,
    amount REAL,
    payment_method TEXT
);