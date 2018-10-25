import sqlite3
import easygui

db = "newnum.db"

def query_user():
    while True:
        try:
            with sqlite3.connect(db) as connection:
                cursor = connection.cursor()
            choice = easygui.buttonbox("Please choose the operation to perform on the data", "Database operation",
                              ("AVG", "MAX", "MIN", "SUM", "Exit"))
            if choice == "Exit":
                print("Exiting...")
                break
            else:
                sql = "select " + choice + "(num) from numbers"
                cursor.execute(sql)
                result = cursor.fetchone()
                easygui.msgbox("The result is: {}".format(str(result[0])),"Press to continue")
        except Exception as e:
            print(e)

query_user()        
