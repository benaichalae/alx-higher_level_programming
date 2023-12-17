#!/usr/bin/python3
"""
script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password>\
                <database> <state_name>".format(argv[0]))
        exit(1)

    username, password, database, state_name = argv[1:]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    connection.close()
