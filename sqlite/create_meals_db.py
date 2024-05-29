# NOTE: create_meals_db.py uses the sqlite3 module to create a new SQLite database called meals.db and populates it with the schema and data from the meals.sql file.
import sqlite3

connection = sqlite3.connect("meals.db")
cursor = connection.cursor()

with open("meals.sql", "r") as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)
connection.commit()
connection.close()
