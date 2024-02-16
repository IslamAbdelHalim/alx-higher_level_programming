#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb

# Create a connection with the database
db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Islam2908$",
        database="hbtn_0e_0_usa")

# Create a cursor
cursor = db.cursor()

# Execute the statment
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

# fetchall
for value in cursor.fetchall():
    print(value)
