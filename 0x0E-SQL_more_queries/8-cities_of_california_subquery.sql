-- Script which lists all cities of CA found in the database
SELECT id, name FROM cities WHERE state_id = 1 ORDER BY cities.id ASC;
