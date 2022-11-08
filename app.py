from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime
import sqlite3
from csv import DictReader
import json
import os

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

@app.route("/downdetector", methods = ["GET", "POST"])
def downdetector():
    return render_template("downdetector.html")

@app.route("/downdetectornav", methods = ["GET", "POST"])
def downdetectornav():
    conn = getdbconnection()
    buildings = conn.execute('SELECT * FROM Buildings').fetchall()

    buildingsData = []
    for building in buildings:
        buildingsData.append({'name': building['name']})
    
    conn.close()
    return render_template("downdetectornav.html", buildingsData = buildingsData)



if __name__ == "__main__":
    app.run()
