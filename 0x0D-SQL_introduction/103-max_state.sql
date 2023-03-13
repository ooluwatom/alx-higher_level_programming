-- Script that displays the max temp of each state
-- by city ordered by STATE

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state DESC;
