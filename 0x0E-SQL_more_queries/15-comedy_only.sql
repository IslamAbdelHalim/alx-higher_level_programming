-- This query returns the titles of all TV shows that are in the 'Comedy' genre, sorted in alphabetical order.

SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
