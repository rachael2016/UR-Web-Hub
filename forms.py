from wtforms import BooleanField, SubmitField, ValidationError, TextAreaField, EmailField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo, DataRequired, Length

class UserReport(FlaskForm):
    status = BooleanField("Down Status", validators=[DataRequired()])
    submit = SubmitField("Submit")

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")