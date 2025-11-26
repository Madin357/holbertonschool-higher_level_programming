-- List all genres and the number of shows linked to each
-- Must use only one SELECT
-- Do not include genres with zero shows
-- Sort by number of shows in descending order

SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

