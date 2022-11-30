import sqlite3, csv, csvfiles
import os
from app import getdbconnection

conn = getdbconnection()
buildings = conn.execute('SELECT * FROM Buildings').fetchall()

buildingsData = []
for building in buildings:
    buildingsData.append({'name': building['name'], 'xcoord' : building['xcoord'], 'ycoord' : ['ycoord']})
    
conn.close()

with open('maphotspotautogen.txt') as f:
    for building in buildingsData:
        #here will go the href and coordinate info
        f.write('')
