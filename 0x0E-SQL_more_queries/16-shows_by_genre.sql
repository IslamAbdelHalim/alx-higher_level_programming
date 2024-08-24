-- This query returns a list of all TV shows in the database, sorted by title, and their genres. If a show has no genre, the genre column should contain the string 'NULL'.

SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;
