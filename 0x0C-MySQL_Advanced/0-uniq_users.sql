-- a SQL script that creates a table users following certain requirments
-- Creates the TABLE
CREATE TABLE users IF NOT EXISTS(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)
