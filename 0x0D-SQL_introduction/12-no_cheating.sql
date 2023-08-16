-- Lists all records of the table `second_table` where `score` >= 10
-- updates score of 'Bob' to 10 using id.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
