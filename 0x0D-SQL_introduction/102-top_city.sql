-- Script displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avr_temp FROM temperatures WHERE month IN ("July", "August") GROUP BY CITY ORDER BY avg_temp DESC LINIT 3;
