#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    with MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306) as db:
        with db.cursor() as cursor:
            cursor.execute("""
                    SELECt cities.id, cities.name, states.name
                    From cities
                    INNER JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC """)
            for value in cursor.fetchall():
                print(value)
