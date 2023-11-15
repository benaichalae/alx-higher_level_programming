--  lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities AS state_name
INNER JOIN states AS state_name ON cities.state_id = states.id
ORDER BY cities.id;
