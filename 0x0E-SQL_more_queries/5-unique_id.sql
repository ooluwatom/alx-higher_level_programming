-- Create table with default/unique id field and database name passed as argument on mysql command
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
