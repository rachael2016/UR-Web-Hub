import sqlite3, csv, csvfiles
import os

connection = sqlite3.connect('databases.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

with open(r'csvfiles\buildings.csv') as fin:
    dr = csv.reader(fin)
    dr = list(dr)
    for i in dr:
        cur.execute("INSERT INTO Buildings(name) VALUES (?);", i)

print("complete")
connection.commit()
connection.close()