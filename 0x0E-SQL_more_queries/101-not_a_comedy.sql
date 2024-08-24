-- Title: Not a Comedy

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name != 'Comedy'
ORDER BY tv_shows.title ASC;
