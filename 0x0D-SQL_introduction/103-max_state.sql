-- Script that displays the max temperature of each state (ordered by State name).
SELECT state MAX(value) As max_temp FROM temperatures ORDER BY state;
