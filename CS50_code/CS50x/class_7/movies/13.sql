--write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred
SELECT name FROM people WHERE id IN
    (SELECT DISTINCT person_id from stars
        WHERE movie_id IN
            (SELECT movie_id FROM stars
            WHERE person_id IN (SELECT id FROM people WHERE name LIKE '%Kevin Bacon%' AND birth == '1958'))
        AND person_id NOT IN (SELECT id FROM people WHERE name LIKE '%Kevin Bacon%' AND birth == '1958')
    )