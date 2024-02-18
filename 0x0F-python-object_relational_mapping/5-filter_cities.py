#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                database=sys.argv[3],
                port=3306)
    cursor = db.cursor()
    cursor.execute(
            """
            SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """, (sys.argv[4],))

    cities = cursor.fetchall()

    cityName = [city[0] for city in cities]

    print(', '.join(cityName))

    cursor.close()
    db.close()
