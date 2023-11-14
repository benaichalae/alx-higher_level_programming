-- Import in hbtn_0c_0 database table dump
SELECT city, AVG(temperature) as avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
