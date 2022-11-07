import sqlite3, csv
import os

connection = sqlite3.connect('databases.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

print("complete")
connection.commit()
connection.close()