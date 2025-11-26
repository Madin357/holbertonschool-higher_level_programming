-- List all shows with their genres (NULL if no genre exists)
-- Output: tv_shows.title - tv_show_genres.genre_id
-- Must use only one SELECT statement
-- Sorted by title ASC and genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

