import sqlite3, csv, csvfiles
import os
from app import getdbconnection

conn = getdbconnection()
buildings = conn.execute('SELECT * FROM Buildings').fetchall()

buildingsData = []
count = 1
for building in buildings:
    buildingsData.append({'name': building['name'], 'xcoord' : building['xcoord'], 'ycoord' : building['ycoord'], 'id' : count})
    count += 1
    
conn.close()

with open('maphotspotautogen.txt', 'w') as f:
    for building in buildingsData:
        #here will go the href and coordinate info
        aherf = '<area target="" alt="" title="" href="downdetector/' + str(building.get("id")) + '"coords="'+ str(building.get("xcoord")) + ','+ str(building.get("ycoord")) + ',8" shape="circle">\n'
        print(aherf)
        f.write(aherf)

f.close()
