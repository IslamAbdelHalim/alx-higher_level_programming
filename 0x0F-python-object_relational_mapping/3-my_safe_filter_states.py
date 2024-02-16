#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    with MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3],
            port=3305) as db:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM states WHERE\
                    name = %s ORDER BY ID ASC;", (sys.argv[4],))
            for value in cursor.fetchall():
                print(value)
