-- Show the rating of each show

SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM hbtn_0d_tvshows_rate
JOIN tv_shows ON hbtn_0d_tvshows_rate.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
