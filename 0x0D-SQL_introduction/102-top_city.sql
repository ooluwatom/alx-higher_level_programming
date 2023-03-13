-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- by city ordered by temperature (descending) with top 3 tempertures

SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
SELECT TOP 3 * FROM temperatures;
