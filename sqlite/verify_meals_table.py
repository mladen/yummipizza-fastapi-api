# verify_meals_table.py
import sqlite3

connection = sqlite3.connect("meals.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='meals';")
table_exists = cursor.fetchone()

if table_exists:
    print("Table 'meals' exists.")
else:
    print("Table 'meals' does not exist.")

connection.close()
