-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- by city ordered by temperature (descending) with top 3 tempertures

SELECT TOP 3 city, AVG(value) as avg_temp FROM temperatures WHERE month ='7' or month = '8' GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
