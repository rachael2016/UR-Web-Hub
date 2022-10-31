from flask import Flask, render_template , json, redirect, url_for, request, flash, session, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError, DateField
from datetime import datetime
import os

app = Flask(__name__ , template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = "placeholder"

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
    return "html template to be added"

if __name__ == "__main__":
    app.run()
