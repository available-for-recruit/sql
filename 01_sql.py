# Create an SQLite3 database and table

import sqlite3

# create a new database if not existing
conn = sqlite3.connect("new.db")

# get a cursor
cursor = conn.cursor()

# create a table
cursor.execute( """
                    CREATE TABLE population (
                    city TEXT,
                    state TEXT,
                    population INT
                    )
                """
               )

conn.close()
