-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- by city ordered by temperature (descending)

SELECT city, AVG(value) as avg_temp FROM temperatures ORDER BY city DESC;
