-- This query should return the genre of the TV show Dexter. The genre should be returned in alphabetical order.

SELECT name
FROM tv_genres
LEFT JOIN tv_shows_genres
ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows
ON tv_shows.id = tv_shows_genres.show_id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
