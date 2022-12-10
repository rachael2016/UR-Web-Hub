from wtforms import BooleanField, SubmitField, ValidationError, TextAreaField, EmailField, StringField, IntegerField, SelectField
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
    # keys = ["Accounting", "Anthropology", "Art History", 
    #     "Biology", "Brain & Cognitive Sciences", "Business", 
    #     "Chemical Engineering", "Chemistry", "Computer Science", 
    #     "Economics", "Education", "English", 
    #     "Finance", "Geography", "Geology", "History", "Linguistics", 
    #     "Marketing", "Mathematics", "Music", "Nursing", 
    #     "Philosophy", "Physics", "Political Science", "Psychology",
    #     "Studio Arts", "Theater", "Women's Studies", "Writing"]
    # tuples = []
    # for i in keys:
    #     tuples.append((i , i))
    abbreviation = StringField("Abbreviation", validators=[DataRequired()])
    course = StringField("Course", validators=[DataRequired()])
    # department = SelectField("Department", choices = tuples)
    professor = StringField("Professor", validators = [DataRequired()])
    submit = SubmitField("Submit")




