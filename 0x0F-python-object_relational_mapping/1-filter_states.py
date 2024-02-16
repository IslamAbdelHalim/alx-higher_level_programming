#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    with MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3306) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
            for value in cursor:
                print(value)
