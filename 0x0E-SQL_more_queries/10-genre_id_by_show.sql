-- Script that lists all shows with  at least one linked genre after importing the db
SELECT tv_shows.title, tv_show_genres.genre_id 
	FROM tv_genres
	JOIN tv_show_genres
	JOIN tv_shows
	ON tv_shows.id = show_id AND tv_genres.id = genre_id
	ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
