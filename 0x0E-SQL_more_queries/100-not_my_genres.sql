-- This query should return all genres that are not associated with the show Dexter.

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.id
WHERE tv_shows.title != 'Dexter'
OR tv_shows.title IS NULL
ORDER BY tv_genres.name ASC;
