-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows OUTER JOIN tv_show_genres ON tv_show_genres.genre_id IS NULL
