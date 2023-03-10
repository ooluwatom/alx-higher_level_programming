--  Script that displays all the  records in the table second_table
-- Displays in descending order of score with score and name

SELECT score, name
FROM second_table
GROUP BY `score` DESC;
