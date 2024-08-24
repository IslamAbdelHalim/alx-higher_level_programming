-- This query returns the title of each TV show and the genre_id of each show. The results are ordered by the title of the TV show in ascending order and the genre_id in ascending order.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
