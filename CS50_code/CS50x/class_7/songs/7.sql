--write a SQL query that returns the average energy of songs that are by Drake
SELECT AVG(energy) FROM songs
    WHERE artist_id in (SELECT id FROM artists WHERE name LIKE "%Drake%");