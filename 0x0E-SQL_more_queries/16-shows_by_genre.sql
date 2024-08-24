-- This query returns a list of all TV shows in the database, sorted by title, and their genres. If a show has no genre, the genre column should contain the string 'NULL'.

SELECT t.`title`, g.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s
ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g
ON s.`genre_id` = g.`id`
ORDER BY t.`title`, g.`name`;
