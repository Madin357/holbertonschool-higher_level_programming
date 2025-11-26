-- List all cities of California
-- California's ID is not known, so we find it with a subquery
-- No JOIN keyword is used
-- Results sorted by cities.id

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    -- Select the id of the state named "California"
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;

