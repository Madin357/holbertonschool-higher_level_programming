-- List all shows and their linked genres
-- If a show has no genre, display NULL
-- Must use only one SELECT statement
-- Sorted by show title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

