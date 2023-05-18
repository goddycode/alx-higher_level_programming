-- Script which creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server

-- Creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL))
