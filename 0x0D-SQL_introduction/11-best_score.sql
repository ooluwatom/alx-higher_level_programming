-- Lists all records of the table `second_table` where `score` >= 10
-- of the database `hbtn_0c_0` in MySQL Server.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
