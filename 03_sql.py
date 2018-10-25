import sqlite3

def create_cities():
    try:
        with sqlite3.connect("new.db") as connection:
            c = connection.cursor()

            # insert multiple records using tuples
            cities = [
                ('Boston', 'MA', 600000),
                ('Los Angeles', 'CA', 38000000),
                ('Houston', 'TX', 2100000),
                ('Philadelphia', 'PA', 1500000),
                ('San Antonio', 'TX', 1400000),
                ('San Diego', 'CA', 130000),
                ('Dallas', 'TX', 1200000),
                ('San Jose', 'CA', 900000),
                ('Jacksonville', 'FL', 800000),
                ('Indianapolis', 'IN', 800000),
                ('Austin', 'TX', 800000),
                ('Detroit', 'MI', 700000)
                ]

            c.executemany(
                """
                    INSERT INTO population
                    VALUES(?, ?, ?)
                    """,
                cities
                )
    except Exception as e:
        print(e)

def create_regions():
    try:
        with sqlite3.connect("new.db") as connection:
            c = connection.cursor()

            c.execute(
                """
                CREATE TABLE regions (city TEXT, region TEXT)
                """
                )
            regions = [
                ('New York City', 'Northeast'),
                ('San Francisco', 'West'),
                ('Chicago', 'Midwest'),
                ('Houston', 'South'),
                ('Phoenix', 'West'),
                ('Boston', 'Northeast'),
                ('Los Angeles', 'West'),
                ('Houston', 'South'),
                ('Philadelphia', 'Northeast'),
                ('San Antonio', 'South'),
                ('San Diego', 'West'),
                ('Dallas', 'South'),
                ('San Jose', 'West'),
                ('Jacksonville', 'South'),
                ('Indianapolis', 'Midwest'),
                ('Austin', 'South'),
                ('Detroit', 'Midwest')
            ]
            c.executemany("INSERT INTO regions VALUES(?, ? )", regions)
            c.execute("SELECT * FROM regions ORDER BY region ASC")
            rows = c.fetchall()
            for r in rows:
                print(r[0], r[1])
    except Exception as e:
        print(e)

# create_cities()
# create_regions()


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute(
        """
        SELECT population.city, population.population,
                regions.region
        FROM population, regions
        WHERE population.city = regions.city
        """
        )
    regions = c.fetchall()
    for region in regions:
        print("City: " + region[0])
        print("Population: " + str(region[1]))
        print("Region: " + str(region[2]))
        print("")
        


