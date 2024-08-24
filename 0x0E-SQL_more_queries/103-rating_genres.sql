-- Query all genres and their rating based on the given rating system

SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
JOIN hbtn_0d_tvshows_rate ON tv_genres.id = hbtn_0d_tvshows_rate.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;