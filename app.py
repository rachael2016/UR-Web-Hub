from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime, timedelta
import sqlite3
from csv import DictReader
from flask_recaptcha import ReCaptcha
import json
import os

from forms import UserReport, FeedbackForm, CourseFeedbackForm

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"
app.config['RECAPTCHA_SITE_KEY'] = "6Le4k20jAAAAAL52Yvi0zAlUMeIgO_ZTBuJozQ6s"
app.config['RECAPTCHA_SECRET_KEY'] = "6Le4k20jAAAAAA-0g_AoWXx9rGjtTYtJi7BomBZ2"
recaptcha = ReCaptcha(app)


def getdbconnection():
    conn = sqlite3.connect('databases.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dining", methods = ["GET", "POST"])
def dining():
    return render_template("dining.html")

@app.route("/ratemycourse", methods = ["GET", "POST"])
def ratemycourse():
    return render_template("ratemycourse.html")

@app.route("/ratemycoursefeedback", methods = ["GET", "POST"])
def coursefeedbackform():
    form = CourseFeedbackForm()
    conn = getdbconnection()
    # conn.execute('INSERT INTO Courses (name, professor, abbreviation, department) VALUES (?, ?, ?, ?)', (form.course.data, form.professor.data, form.abbreviation.data, form.department.data))
    # ratings = conn.execute("SELECT * FROM Courses WHERE department = ?", (form.department.data,)).fetchall()
    # ratingsList = []
    # for rating in ratings:
    #     ratingsList.append({'name': \
    #         rating['name'], 'professor': rating['professor'], \
    #         'abbreviation': rating['abbreviation'], 'department': rating['department']})
    # print(ratingsList)
    # conn.commit()
    # conn.close()
        
    if form.validate_on_submit():
        conn = getdbconnection()
        conn.execute('INSERT INTO Courses (name, professor, abbreviation, department) VALUES (?, ?, ?, ?)', (form.course.data, form.professor.data, form.abbreviation.data, form.department.data))
        ratings = conn.execute("SELECT * FROM Courses WHERE department = ?", (form.department.data,)).fetchall()
        ratingsList = []
        for rating in ratings:
            ratingsList.append({'name': \
                rating['name'], 'professor': rating['professor'], \
                'abbreviation': rating['abbreviation'], 'department': rating['department']})
        print(ratingsList)
        conn.commit()
        conn.close()
        print(form.rating.data)
        print(form.difficulty.data)
        print(form.usefulness.data)
        print(form.online.data)
        print(form.review.data)
        # print(request.form.get('dropMenu'))
        print(request.form.getlist('tag'))
        print(form.review.data)
        form.course.data = ''
        form.professor.data = ''
        form.abbreviation.data = ''
        form.department.data = ''
        return redirect(url_for('ratemycourse'))
    else:
        print("form invalid")
    return render_template("ratemycoursefeedback.html", form = form)

# 3 ,adfs,asdf,asdf
# variable = "CSC 171"
# courseid = conn.execute(SELECT id from Courses where abbreviation = )
# (SELECT * FROM CourseRatingsReceived WHERE couseid = (SELECT id from Courses where abbreviation = ""))
# @app.route("/courseratingfeedbackform", methods = ["GET", "POST"])
# def courseratingfeedbackform():
#     form = CourseRatingFeedbackForm()
#     if form.validate_on_submit():
#         conn = getdbconnection()
#         conn.execute('INSERT INTO CourseRatingsReceived (courseid, rating, message, tips) \
#         VALUES ((SELECT id from Courses WHERE abbreviation = ?), ?, ?, ?)', 
#         (form.abbreviation.data, form.rating.data, form.message.data, form.tips.data))
#         conn.close()
#         form.abbreviation.data = ''
#         form.rating.data = ''
#         form.message.data = ''
#         form.tips.data = ''
#         return redirect(url_for('ratemycourse'))
#     else: 
#         print("form invalid")
#     return render_template("coursefeedbackform.html", form = form)

# @app.route("/ratemycourseadd", methods = ["GET", "POST"])
# def ratemycourseadd():
#     return render_template("ratemycourseadd.html")

# @app.route("/ratemycoursefeedback", methods = ["GET", "POST"])
# def ratemycoursefeedback():
#     return render_template("ratemycoursefeedback.html")

# conn = getdbconnection()
    # buildings = conn.execute('SELECT * FROM Buildings').fetchall()

    # buildingsData = []
    # for building in buildings:
    #     buildingsData.append({'name': building['name'], 'buildingid' : building['buildingid']})
    
    # conn.close()
    # return render_template("buildinglist.html", buildings = buildingsData)

# courses - dep, name, professor, abbr
# coursesratings - courseid, rating, message, tips
@app.route("/ratemycourseratings", methods = ["GET", "POST"])
def ratemycourseratings():
    conn = getdbconnection()
    reviews = conn.execute('SELECT * FROM CourseRatingsReceived').fetchall()

    reviewsData = []
    for review in reviews:
        reviewsData.append({'rating': reviews['rating'], 'message': reviews['message'], \
            'tips': reviews['tips'], 'courseid': reviews['courseid']})
    conn.close()
    return render_template("ratemycourseratings.html", reviews = reviewsData)

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
    reportcount = 0
    for i in range(0, 24):
        minusHour = iteratetime - timedelta(hours=1)
        downstatus = True
        temprecords = conn.execute('SELECT * FROM ElevatorDownRecords WHERE buildingid = ? AND datetime >= ? AND datetime < ? AND down = ?', (buildingid, minusHour, iteratetime, downstatus)).fetchall()
        recordcount = 0
        if temprecords:
            for record in temprecords:
                recordcount += 1
                reportcount += 1

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

    for record in recentrecords:
        recordentry = {
            "id": record['recordid'],
            "datetime": record['datetime'],
            "down": record['down']
        }
        allrecentrecords.append(recordentry)

    #form for reports
    form = UserReport()
    if form.validate_on_submit():
        status = form.status.data
        conn = getdbconnection()
        conn.execute('INSERT INTO ElevatorDownRecords (buildingid, datetime, down) VALUES (?, ?, ?)', (buildingid, datetime.now(), status))
        conn.commit()
        conn.close()
        print("down detector report successfully recieved")
        form.status.data = ''
        status = ''
        return render_template("downdetectorrefresh.html", buildingid = buildingid)
    elif form.status.data == False and request.method == "POST":
        status = form.status.data
        conn = getdbconnection()
        conn.execute('INSERT INTO ElevatorDownRecords (buildingid, datetime, down) VALUES (?, ?, ?)', (buildingid, datetime.now(), status))
        conn.commit()
        conn.close()
        print("down detector report successfully recieved")
        form.status.data = ''
        status = ''
        return render_template("downdetectorrefresh.html", buildingid = buildingid)
    #for debugging purposes
    else:
        print(form.status.data)
        print("form invalid")
    
    form.status.data = ''
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

@app.route("/buildinglist", methods = ["GET"])
def buildinglist():
    conn = getdbconnection()
    buildings = conn.execute('SELECT * FROM Buildings').fetchall()

    buildingsData = []
    for building in buildings:
        buildingsData.append({'name': building['name'], 'buildingid' : building['buildingid']})
    
    conn.close()
    return render_template("buildinglist.html", buildings = buildingsData)

@app.route("/thanksforreporting")
def thanksforreporting():
    return render_template("downdetectorrefresh.html")

@app.route("/feedbackform", methods = ["GET", "POST"])
def feedbackform():
    form = FeedbackForm()
    form.status.data = ''
    if form.validate_on_submit() and recaptcha.verify():
        conn = getdbconnection()
        now = datetime.now()
        conn.execute('INSERT INTO GeneralFeedbackReceived (name, email, subject, message, datetime) VALUES (?, ?, ?, ?, ?)', (form.name.data, form.email.data, form.subject.data, form.message.data, now))
        ratings = conn.execute('SELECT * FROM GeneralFeedbackReceived').fetchall()
        ratingsList = []
        for rating in ratings:
            ratingsList.append({'name': \
                rating['name'], 'email': rating['email'], \
                'subject': rating['subject']})
        print(ratingsList)
        conn.commit()
        conn.close()
        form.name.data = ''
        form.email.data = ''
        form.subject.data = ''
        form.message.data = ''
        return redirect(url_for('feedbackthankyou'))

    else:
        print("form invalid")

    return render_template("feedbackform.html", form = form)

@app.route("/feedbackthankyou")
def feedbackthankyou():
    return render_template("feedbackformthanks.html")




if __name__ == "__main__":
    app.run(debug=True)
    
