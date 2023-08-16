-- Script that lists all cities found in  in the database in an order
SELECT DISTINCT cities.id, cities.name, states.name 
	FROM cities JOIN (states) ON cities.state_id = states.id
	ORDER BY id ASC;
