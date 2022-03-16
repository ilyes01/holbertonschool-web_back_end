--SQL script that creat a table users 
--script should not fail if the table already exists
CREATE TABLE if NOT EXISTS users (
id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255)
);

