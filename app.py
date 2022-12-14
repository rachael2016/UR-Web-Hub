from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime, timedelta
import sqlite3
from csv import DictReader
from flask_recaptcha import ReCaptcha
import json
import os

from forms import UserReport, FeedbackForm, CourseFeedbackForm, HomeForm, DiningFeedbackForm

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

@app.route("/diningfeedbackform", methods = ["GET", "POST"])
def diningfeedbackform():
    form = DiningFeedbackForm()
    if form.validate_on_submit() and recaptcha.verify():
        conn = getdbconnection()
        now = datetime.now()
        conn.execute('INSERT INTO DiningFeedbackReceived (location, comment) VALUES (?, ?)', (form.location.data, form.comment.data))
        conn.commit()
        conn.close()
        form.location.data = ''
        form.comment.data = ''
        return redirect(url_for('feedbackthankyou'))

    else:
        print("form invalid")

    return render_template("diningfeedback.html", form = form)

@app.route("/ratemycourse", methods = ["GET", "POST"])
def ratemycourse():
    form = HomeForm()
    if form.validate_on_submit():
        conn = getdbconnection()
        ratings = conn.execute("SELECT * FROM Courses WHERE department = ?", (form.department.data,)).fetchall()
        conn.close()
        for rating in ratings:
            if form.abbreviation.data in rating['abbreviation']:
                return redirect(url_for("ratemycourseratings", courseID = form.abbreviation.data))
                # return redirect(url_for('dashboard', abbreviation = form.abbreviation.data))
        conn.close()
        return render_template("ratemycourse.html", form = form, bool = True)
    else:
        print("invalid form")
    return render_template("ratemycourse.html", form = form, bool = False)

# @app.route("/ratemycoursefeedback/<courseAbbrev>", methods = ["GET", "POST"])
@app.route("/ratemycoursefeedback", methods = ["GET", "POST"])
def coursefeedbackform():
    form = CourseFeedbackForm()
    # conn = getdbconnection()      
    if form.validate_on_submit():
        conn = getdbconnection()
        conn.execute('INSERT INTO Courses (name, professor, abbreviation, department) VALUES (?, ?, ?, ?)', (form.course.data, form.professor.data, form.abbreviation.data, form.department.data))
        if len(request.form.getlist('tag')) > 0:
            str1 = ','.join(request.form.getlist('tag'))
            print(str1)
            conn.execute('INSERT INTO CourseRatingsReceived (courseid, rating, message, difficulty, usefulness, tags, semester, professor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
        (form.abbreviation.data, form.rating.data, form.review.data, form.difficulty.data, form.usefulness.data, str1, form.semester.data, form.professor.data))
        else:
            conn.execute('INSERT INTO CourseRatingsReceived (courseid, rating, message, difficulty, usefulness, semester, professor) VALUES (?, ?, ?, ?, ?, ?, ?)', 
        (form.abbreviation.data, form.rating.data, form.review.data, form.difficulty.data, form.usefulness.data, form.semester.data, form.professor.data))

        ratings = conn.execute("SELECT * FROM CourseRatingsReceived").fetchall()
        ratingsList = []
        for rating in ratings:
            ratingsList.append({'tags': rating['tags']})
        # print(ratingsList)
        conn.commit()
        conn.close()
        # print(form.rating.data)
        # print(form.difficulty.data)
        # print(form.usefulness.data)
        # print(form.online.data)
        # print(form.review.data)
        # print(request.form.get('dropMenu'))
        # print(request.form.getlist('tag'))
        # print(request.form.getlist('tag')[0])
        print(form.review.data)
        temp = form.abbreviation.data
        form.course.data = ''
        form.professor.data = ''
        form.abbreviation.data = ''
        form.department.data = ''
        # return redirect(url_for('ratemycourse'))
        return redirect(url_for("ratemycourseratings", courseID = temp))
    else:
        print("form invalid")
    return render_template("ratemycoursefeedback.html", form = form)

@app.route("/ratemycourseratings/<courseID>", methods = ["GET", "POST"])
def ratemycourseratings(courseID):
    conn = getdbconnection()
    reviews = conn.execute('SELECT * FROM CourseRatingsReceived WHERE courseID = ?', (courseID,)).fetchall()
    # reviewsData = []
    fiveStars = 0
    fourStars = 0
    threeStars = 0
    twoStars = 0
    oneStar = 0
    totalRatings = 0
    totalDifficulty = 0
    totalUsefulness = 0
    messages = []
    reviewDict = []
    spam_list = []
    for review in reviews:
        reviewDict.append({'rating': review['rating'], 'message': review['message'], 'semester' : review['semester'], \
            'professor' : review['professor'], 'difficulty' : review['difficulty'], 'usefulness' : review['usefulness']})
        # print(review['rating'])
        # print(review['message'])
        rating = int(review['rating'])
        difficulty = int(review['difficulty'])
        usefulness = int(review['usefulness'])
        # temp = list(review['tags'])
        # if(len(review['tags']) == 1):
        #     spam_list.append(review['tags'][0])
        # else:
        spam_list = str(review['tags']).split(',')
        print(spam_list)
        if(rating == 5):
            fiveStars += 1
        elif rating == 4:
            fourStars += 1
        elif rating == 3:
            threeStars += 1
        elif rating == 2:
            twoStars += 1
        elif rating == 1:
            oneStar += 1
        totalRatings += rating
        totalDifficulty += difficulty
        totalUsefulness += usefulness
        messages.append(review['message'])
    # print("size", len(reviews))
    if(len(reviews) == 0):
        average = 0
        averageDiff = 0
        averageUse = 0
    else:
        average = totalRatings / len(reviews)
        averageDiff = totalDifficulty / len(reviews)
        averageUse = totalUsefulness / len(reviews)
    conn.close()
    # print(messages)
    return render_template("ratemycourseratings.html", courseID = courseID, overall = average,
    numRatings = len(reviews), five_stars = fiveStars, four_stars = fourStars, 
    three_stars = threeStars, two_stars = twoStars, one_star = oneStar,difficulty = averageDiff, 
    usefulness = averageUse, tags = spam_list, reviews = reviewDict)

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
    for i in range(1, 24):
        minusHour = iteratetime - timedelta(hours=1)
        downstatus = True
        temprecords = conn.execute('SELECT * FROM ElevatorDownRecords WHERE buildingid = ? AND datetime >= ? AND datetime < ? AND down = ?', (buildingid, minusHour, iteratetime, downstatus)).fetchall()
        recordcount = 0
        if temprecords:
            for record in temprecords:
                recordcount += 1
                reportcount += 1

        tographedrecords = {
            "datetime": "-" + str(i) + "h",
            "reportAmount": recordcount
        }
        graphedrecords.append(tographedrecords)
        iteratetime -= timedelta(hours=1)

    labels = []
    values = []
    for record in graphedrecords:
        labels.append(record["datetime"])
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
    
