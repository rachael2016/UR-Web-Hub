import sqlite3, csv, csvfiles
import os

connection = sqlite3.connect('databases.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

with open(r'csvfiles\buildings.csv') as fin:
    dr = csv.reader(fin)
    dr = list(dr)
    count = 0

    for i in dr:
        if(count == 0):
            count += 1
            continue
        else:
            cur.execute("INSERT INTO Buildings(name) VALUES (?);", i)
            count += 1

print("complete")
connection.commit()
connection.close()