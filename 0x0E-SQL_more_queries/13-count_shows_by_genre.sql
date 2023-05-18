-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_shows.title AS genre, tv_show_genres.genre_id AS number_of_shows FROM tvshow
sLEFT JOIN tv_show_genres 
ON tv_shows_id = tv_show_genres.show_id 
ORDER BY genre ASC, 
number_of_shows ASC;
