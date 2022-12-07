import sqlite3, csv, csvfiles
import os

connection = sqlite3.connect('databases.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

with open(r'csvfiles/buildings.csv') as fin:
    dr = csv.DictReader(fin)
    todb = [(i['name'], i['x'], i['y']) for i in dr]
cur.executemany("INSERT INTO Buildings (name, xcoord, ycoord) VALUES (?, ?, ?);", todb)

print("complete")
connection.commit()
connection.close()