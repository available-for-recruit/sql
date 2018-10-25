import csv
import sqlite3

try:
    with sqlite3.connect("new.db") as connection:
        c = connection.cursor()

        # get employee data from csv
        employees = csv.reader(open("employees.csv", "rU"))
        c.execute(
            """
                CREATE TABLE employees(
                firstname TEXT,
                lastname TEXT)
            """
            )
        c.executemany(
            """
                INSERT INTO employees(
                firstname,
                lastname
                )
                VALUES(
                ?,
                ?
                )
            """
            ,
            employees
            )
except sqlite3.OperationalError as e:
    print("Oops! Something went wrong. Try again: " + str(e))


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    for row in c.fetchall():
        print(row)

    c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")
    c.execute("SELECT * from population")
    for row in c.fetchall():
        print(row)
