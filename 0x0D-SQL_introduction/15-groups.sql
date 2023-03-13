-- Return number of people with thesame score
-- as number

SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
