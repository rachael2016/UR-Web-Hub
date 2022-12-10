from wtforms import BooleanField, SubmitField, ValidationError, TextAreaField, EmailField, StringField, IntegerField
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

class CourseFeedbackForm(FlaskForm):
    department = StringField("department", validators=[DataRequired()])
    course = StringField("course", validators=[DataRequired()])
    professor = StringField("Professor", validators=[DataRequired()])
    abbreviation = StringField("abbreviation", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CourseRatingFeedbackForm(FlaskForm):
    keys = ["Accounting", "Anthropology", "Art History", 
        "Biology", "Brain & Cognitive Sciences", "Business", 
        "Chemical Engineering", "Chemistry", "Computer Science", 
        "Economics", "Education", "English", 
        "Finance", "Geography", "Geology", "History", "Linguistics", 
        "Marketing", "Mathematics", "Music", "Nursing", 
        "Philosophy", "Physics", "Political Science", "Psychology",
        "Studio Arts", "Theater", "Women's Studies", "Writing"]
    for i in keys:
        keys2.append((i,i))
    abbreviation = StringField("abbreviation", validators=[DataRequired()])
    rating = IntegerField("rating", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    tips = TextAreaField("tips", validators=[DataRequired()])
    submit = SubmitField("Submit")


