-- List all shows that have NO genre linked
-- Output: tv_shows.title - tv_show_genres.genre_id (NULL)
-- Must use only one SELECT statement
-- Sorted by title ASC and genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

