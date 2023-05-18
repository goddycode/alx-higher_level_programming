-- Script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on my MySQL server

-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use Database
USE hbtn_0d_usa;

-- Create table cities
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id));
