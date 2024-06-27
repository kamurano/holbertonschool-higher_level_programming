-- SQL
SELECT score, COUNT(name) as number FROM second_table GROUP BY score ORDER BY number DESC;
