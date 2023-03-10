--  Script that inserts a new row in the table first_tablecreates a table second_table
-- Insert new rows
CREATE TABLE IF NOT EXISTS second_table(
    id INT, 
    VARCHAR(256),
    score INT
);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
