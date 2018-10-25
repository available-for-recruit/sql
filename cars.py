import sqlite3

def create_inventory():
    try:
        with sqlite3.connect("cars.db") as connection:
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
    except Exception as e:
        print(str(e))

    try:
        inventory = [
            ('Honda', 'Accord', 3),
            ('Honda', 'Civic', 2),
            ('Ford', 'Ranger', 5),
            ('Ford', 'F150', 3),
            ('Ford', 'Taurus', 7)
            ]
        with sqlite3.connect("cars.db") as connection:
            cursor = connection.cursor()

            cursor.executemany(
                """
                INSERT INTO inventory (
                Make,
                Model,
                Quantity
                )
                VALUES (?,?,?)
                """,
                inventory)
    except Exception as e:
        print(str(e))

def update_inventory():

        cursor.executemany(
            """
            UPDATE inventory
            SET Quantity = ?
            WHERE Make = ?
            AND Model = ?
            """
            ,
            [('8',
            'Honda',
            'Civic')]
            )

        cursor.executemany(
            """
            UPDATE inventory
            SET Quantity = ?
            WHERE Make = ?
            AND Model = ?
            """
            ,
            [('4',
            'Ford',
            'F150',
             )]
            )
        
def create_orders():
    try:
        with sqlite3.connect("cars.db") as connection:
            c = connection.cursor()
            c.execute(
                """
                CREATE TABLE orders (
                make text,
                model text,
                order_date text
                )
                """
                )
            orders = [
                ('Honda','Accord','2018-10-01'),
                ('Honda','Accord','2018-10-02'),
                ('Honda','Accord','2018-10-03'),
                ('Honda','Civic','2018-09-01'),
                ('Honda','Civic','2018-09-02'),
                ('Honda','Civic','2018-09-03'),
                ('Ford','Ranger','2018-08-01'),
                ('Ford','Ranger','2018-08-02'),
                ('Ford','Ranger','2018-08-03'),
                ('Ford','F150','2018-07-01'),
                ('Ford','F150','2018-07-02'),
                ('Ford','F150','2018-07-03')
                ]
            c.executemany(
                """
                INSERT INTO orders (make, model, order_date)
                VALUES (?, ?, ?)
                """,
                orders
                )

    except Exception as e:
        print(e)
        

def display_sql_output(*args):
    with sqlite3.connect("cars.db") as connection:
        cursor = connection.cursor()
        cursor.execute(*args)
        cars = cursor.fetchall()

        for car in cars:
            print(car)

def display_order_details():
    with sqlite3.connect("cars.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT Make, Model, Quantity FROM inventory")
        cars = cursor.fetchall()
        for car in cars:
            # Make, Model
            print("Make: {}, Model: {}".format(car[0], car[1]))
            # Quantity
            print("Quantity: {}".format(str(car[2])))

            cursor.execute("SELECT count(order_date) from orders where make = ? and model = ?", (car[0], car[1]))
            num_orders = cursor.fetchone()
            print("Number of orders: {}".format(num_orders[0]))
            
            cursor.execute("SELECT order_date from orders where make = ? and model = ?", (car[0], car[1]))
            order_dates = cursor.fetchall()
            for order_date in order_dates:
                print("Order date: {}".format(order_date[0]))


# create_inventory()
# create_orders()
display_sql_output("SELECT * FROM inventory")
display_sql_output("SELECT * FROM inventory WHERE Make = ?", ("Ford",))
display_sql_output("SELECT * FROM orders")
display_order_details()
