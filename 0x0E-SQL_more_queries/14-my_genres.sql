-- This query should return the genre of the TV show Dexter. The genre should be returned in alphabetical order.

SELECT tv_genres.name
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
