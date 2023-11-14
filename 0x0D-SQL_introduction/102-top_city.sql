-- Import in hbtn_0c_0 database table dump
SELECT city, AVG(temperature) as avg_temp
FROM temperature_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
