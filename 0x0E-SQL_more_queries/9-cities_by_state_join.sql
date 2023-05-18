-- Script which list all cities contained in the database hbtn_0d_usa
-- List all rows of some columns from database

SELECT cities.id, cities.name, states.id FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
