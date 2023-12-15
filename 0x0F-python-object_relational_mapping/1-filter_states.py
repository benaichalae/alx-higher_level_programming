#!/usr/bin/python3
"""Script to list all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name \
            LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
