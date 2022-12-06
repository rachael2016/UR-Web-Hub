from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime, timedelta
import sqlite3
from csv import DictReader
import json
import os

from forms import UserReport, FeedbackForm

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"

def getdbconnection():
    conn = sqlite3.connect('databases.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dietaryneedfinder", methods = ["GET", "POST"])
def dining():
    return render_template("dining.html")

@app.route("/ratemycourse", methods = ["GET", "POST"])
def ratemycourse():
    return render_template("ratemycourse.html")

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
    
    #Getting data for graph
    graphedrecords = []
    iteratetime = datetime.now()
    for i in range(0, 24):
        minusHour = iteratetime - timedelta(hours=1)
        temprecords = conn.execute('SELECT * FROM ElevatorDownRecords WHERE buildingid = ? AND datetime >= ? AND datetime < ?', (buildingid, minusHour, iteratetime)).fetchall()
        recordcount = 0
        if temprecords:
            for record in temprecords:
                recordcount += 1

        tographedrecords = {
            "datetime": minusHour,
            "reportAmount": recordcount
        }
        graphedrecords.append(tographedrecords)
        iteratetime -= timedelta(hours=1)

    labels = []
    values = []
    for record in graphedrecords:
        time = "%s:%s" % (record["datetime"].hour, record["datetime"].minute)
        labels.append(time)
        values.append(record["reportAmount"])
    
    conn.close()

    #Invalid building name/id
    if not name:
        return "404"

    #taking all reports and recent reports and looping for formatting after being taken from database
    allreports = []

    for report in reports:
        reportentry = {
            "id": report['recordid'],
            "datetime": report['datetime'],
            "down": report['down']
        }
        allreports.append(reportentry)

    allrecentrecords = []
    reportcount = 0

    for record in recentrecords:
        reportcount += 1
        recordentry = {
            "id": record['recordid'],
            "datetime": record['datetime'],
            "down": record['down']
        }
        allrecentrecords.append(recordentry)

    #form for reports
    status = None
    form = UserReport()
    if form.validate_on_submit():
        status = form.status.data
        conn = getdbconnection()
        conn.execute('INSERT INTO ElevatorDownRecords (buildingid, datetime, down) VALUES (?, ?, ?)', (buildingid, datetime.now(), status))
        conn.commit()
        conn.close()
        print("down detector report successfully recieved")
        form.status.data = None
        status = None
        return render_template("downdetector.html", allreports = allreports, allrecentrecords = allrecentrecords, form = form,
        name = name, reportcount = reportcount)
    #for debugging purposes
    else:
        print("form invalid")
    
    return render_template("downdetector.html", allreports = allreports, allrecentrecords = allrecentrecords, form = form,
        name = name, reportcount = reportcount, labels = labels, values = values)

@app.route("/downdetectornav", methods = ["GET", "POST"])
def downdetectornav():
    conn = getdbconnection()
    buildings = conn.execute('SELECT * FROM Buildings').fetchall()

    buildingsData = []
    for building in buildings:
        buildingsData.append({'name': building['name'], 'xcoord' : building['xcoord'], 'ycoord' : ['ycoord']})
    
    conn.close()
    return render_template("downdetectornav.html", buildingsData = buildingsData)

@app.route("/feedbackform", methods = ["GET", "POST"])
def feedbackform():
    form = FeedbackForm()
    if form.validate_on_submit():
        conn = getdbconnection()
        now = datetime.now()
        conn.execute('INSERT INTO GeneralFeedbackReceived (name, email, subject, message, datetime) VALUES (?, ?, ?, ?, ?)', (form.name.data, form.email.data, form.subject.data, form.message.data, now))
        conn.close()
        form.name.data = ''
        form.email.data = ''
        form.subject.data = ''
        form.message.data = ''

    else:
        print("form invalid")

    return render_template("feedbackform.html", form = form)

if __name__ == "__main__":
    app.run()
