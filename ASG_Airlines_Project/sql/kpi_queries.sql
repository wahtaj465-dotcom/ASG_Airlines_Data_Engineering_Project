-- KPI Queries
-- ==========================================
-- KPI 1 : Flights by Airline
-- ==========================================

SELECT
    airline,
    COUNT(*) AS total_flights
FROM dim_flights
GROUP BY airline
ORDER BY total_flights DESC;

-- ==========================================
-- KPI 2 : Revenue by Airline
-- ==========================================

SELECT
    f.airline,
    ROUND(SUM(p.amount),2) AS revenue
FROM fact_payments p
JOIN fact_bookings b
ON p.booking_id = b.booking_id
JOIN dim_flights f
ON b.flight_key = f.flight_key
GROUP BY f.airline
ORDER BY revenue DESC;

-- ==========================================
-- KPI 3 : Booking Status
-- ==========================================

SELECT
    status,
    COUNT(*) AS bookings
FROM fact_bookings
GROUP BY status;

-- Continue with the remaining KPI queries...