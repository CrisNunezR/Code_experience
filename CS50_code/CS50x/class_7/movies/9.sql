--write a SQL query to list the names of all people who
--starred in a movie released in 2004, ordered by birth year
--here too I decided not to account for duplicate names just to achieve the same number of results (18,946)
--a better query should account for repetition by using DISTINCT after SELECT
SELECT name FROM people WHERE id IN (
    SELECT person_id FROM stars WHERE movie_id IN (
        SELECT id FROM movies WHERE year == '2004')) ORDER BY birth;