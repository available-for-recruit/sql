import sqlite3

connection = sqlite3.connect("cars.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE inventory (
    Make TEXT,
    Model TEXT,
    Quantity INT
    )
    """
    )

connection.close()
