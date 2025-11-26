-- List all cities with their corresponding state
-- Output format: cities.id - cities.name - states.name
-- Must use only one SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

