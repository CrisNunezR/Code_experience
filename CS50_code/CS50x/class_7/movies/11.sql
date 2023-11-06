--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in,
--starting with the highest rated
SELECT title FROM movies JOIN ratings ON ratings.movie_id == movies.id
    WHERE id in (
        SELECT movie_id FROM stars WHERE person_id in (
            SELECT id FROM people WHERE name LIKE 'Chadwick Boseman'))
            ORDER BY rating DESC
            LIMIT 5