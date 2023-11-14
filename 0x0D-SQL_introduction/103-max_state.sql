--Import in hbtn_0c_0 database table dump
SELECT state, MAX(temperature) as max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;
