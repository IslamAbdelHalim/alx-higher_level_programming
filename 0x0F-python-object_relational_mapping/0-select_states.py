#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

# Create a connection with the database
db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)

# Create a cursor
cursor = db.cursor()

# Execute the statment
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

# fetchall
for value in cursor.fetchall():
    print(value)

cursor.close();
db.close();
