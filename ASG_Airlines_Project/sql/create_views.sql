-- ==========================================
-- View : Route Traffic
-- ==========================================

CREATE VIEW vw_route_traffic AS

SELECT
    source,
    destination,
    COUNT(*) AS total_flights
FROM dim_flights
GROUP BY source, destination;

-- ==========================================
-- View : Airline Performance
-- ==========================================

CREATE VIEW vw_airline_performance AS

SELECT
    airline,
    COUNT(*) AS total_flights,
    ROUND(AVG(duration_minutes),2) AS avg_duration,
    SUM(CASE
            WHEN is_overnight = 1 THEN 1
            ELSE 0
        END) AS overnight_flights
FROM dim_flights
GROUP BY airline;

-- ==========================================
-- View : Booking Summary
-- ==========================================

CREATE VIEW vw_booking_summary AS

SELECT
    b.booking_id,
    p.first_name,
    p.last_name,
    f.airline,
    f.source,
    f.destination,
    b.status,
    f.duration_minutes
FROM fact_bookings b
JOIN dim_passengers p
ON b.passenger_key = p.passenger_key
JOIN dim_flights f
ON b.flight_key = f.flight_key;