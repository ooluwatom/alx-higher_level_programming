-- Script that displays the max temp of each state
-- by city ordered by STATE

SELECT city, MAX(value) as avg_temp FROM temperatures GROUP BY state ORDER BY state DESC;
