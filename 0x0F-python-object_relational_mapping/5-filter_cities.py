#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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

    query = '''
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    '''
    cursor.execute(query, (state_name,))

    result = cursor.fetchone()

    if result[0]:
        print(result[0])
    else:
        print()

    cursor.close()
    connection.close()
