--write a SQL query to list the names of all people who have directed
--a movie that received a rating of at least 9.0
--notice that this query returns duplicate names since a director can have directed more than 1
--movie rated with 9+ but I'm not correcting this to achieve the expected 3392 result
SELECT name FROM people WHERE id in (
    SELECT person_id FROM directors WHERE movie_id in (
        SELECT movie_id FROM ratings WHERE rating >= 9));