#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    for value in cursor.fetchall():
        print(value)
    cursor.close()
    db.close()
