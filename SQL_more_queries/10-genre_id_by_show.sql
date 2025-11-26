-- List all shows that have at least one genre linked
-- Output: tv_shows.title - tv_show_genres.genre_id
-- Only one SELECT statement allowed
-- Results sorted by title ASC, then genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

