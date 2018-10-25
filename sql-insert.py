import random
import sqlite3

db = "newnum.db"
def create_db():
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE numbers(num INT)")
    except Exception as e:
        print(e)

def insert_numbers():
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            for i in range(0,101):
                num = random.randint(0,100)
                cursor.execute("INSERT into numbers(num) VALUES (?)",[num])
                
    except Exception as e:
        print(e)

def display_numbers():
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * from numbers")
            for num in cursor.fetchall():
                print(num)
    except Exception as e:
        print(e)


# create_db()
# insert_numbers()
# display_numbers()
