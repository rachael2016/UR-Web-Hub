from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime, timedelta
import sqlite3
from csv import DictReader
import json
import os

from forms import UserReport

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"

def getdbconnection():
    conn = sqlite3.connect('databases.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/campusnavigator", methods = ["GET", "POST"])
def campusnavigator():
    return "html template to be added"

@app.route("/dietaryneedfinder", methods = ["GET", "POST"])
def dietaryneedfinder():
    return "html template to be added"

@app.route("/downdetector/<int:buildingid>", methods = ["GET", "POST"])
def downdetector(buildingid):

    #Connecting to the database, gets all records within 24 hours
    conn = getdbconnection()
    name = conn.execute('SELECT * FROM Buildings WHERE buildingid = ?', (buildingid,)).fetchone()
    name = name['name']
    reports = conn.execute('SELECT * FROM ElevatorDownRecords WHERE buildingid = ?', (buildingid,)).fetchall()
    now = datetime.now()
    previous = datetime.now() - timedelta(days=1)
    recentrecords = conn.execute('SELECT * FROM ElevatorDownRecords WHERE buildingid = ? AND datetime >= ? AND datetime < ?', (buildingid, previous, now)).fetchall()
    conn.close()

    #Invalid building name/id
    if not name:
        return "404"

    #taking all reports and recent reports and looping for formatting after being taken from database
    allreports = []

    for report in reports:
        reportentry = {
            "id": report['reportid'],
            "datetime": report['datetime'],
            "down": report['down']
        }
        allreports.append(reportentry)

    allrecentrecords = []

    for record in recentrecords:
        recordentry = {
            "id": record['reportid'],
            "datetime": record['datetime'],
            "down": record['down']
        }
        allrecentrecords.append(recordentry)

    #form for reports
    status = None
    form = UserReport()
    if form.validate_on_submit():
        conn = getdbconnection()
        conn.execute('INSERT INTO ElevatorDownRecords (buildingid, datetime, down) VALUES (?, ?, ?)', (buildingid, datetime.now(), form.status))
        conn.commit()
        conn.close()
        status = form.status.data
        form.status.data = None
    #for debugging purposes
    else:
        print("form invalid")
    
    return render_template("downdetector.html", allreports = allreports, allrecentrecords = allrecentrecords, form = form,
        name = name)

@app.route("/downdetectornav", methods = ["GET", "POST"])
def downdetectornav():
    conn = getdbconnection()
    buildings = conn.execute('SELECT * FROM Buildings').fetchall()

    buildingsData = []
    for building in buildings:
        buildingsData.append({'name': building['name'], 'xcoord' : building['xcoord'], 'ycoord' : ['ycoord']})
    
    conn.close()
    return render_template("downdetectornav.html", buildingsData = buildingsData)



if __name__ == "__main__":
    app.run()
