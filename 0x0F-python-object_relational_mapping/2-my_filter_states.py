#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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

    cursor.execute("SELECT * FROM states WHERE \
            name = '{}'".format(sys.argv[4]))

    for value in cursor.fetchall():
        print(value)

    cursor.close()
    db.close()
