from wtforms import BooleanField, SubmitField, ValidationError, TextAreaField, EmailField, StringField, IntegerField, SelectField, RadioField
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo, DataRequired, Length
from wtforms.widgets import TextArea


keys = ["African and African-American Studies", "American Sign Language",
        "American Studies", "Anthropology", "Archaeology, Technology and Historical Structures", 
        "Art History", "Art and Art History", "Audio and Music Engineering", 
        "Biology", "Biomedical Engineering", "Brain & Cognitive Sciences", "Business", 
        "Chemical Engineering", "Chemistry", "Classics, Religion", "Computer Science", 
        "Dance and Movement", "Data Science", "Digital Media Studies", 
        "Earth and Ennvironmental Sciences", "East Asian Studies", "Economics", 
        "Electrical and Computer Engineering", "English", "Environmental Humanities",
        "Film and Media Studies", "Gender, Sexuality, and Women's Studies", "History", 
        "International Theatre", "Linguistics", "Materials Science", "Mathematics", 
        "Mechanical Engineering", "Modern Languages and Cultures", "Music", "Naval Science", 
        "Optics", "Philosophy", "Physics and Astronomy", "Political Science", "Psychology",
        "Public Health", "Religion and Classics", "Russian Studies", "Statistics", 
        "Sustainability Studies", "Theater", "Visual and Cultural Studies", "Writing, Speaking, and Argument"]
tuples = []
for i in keys:
    tuples.append((i , i))

class UserReport(FlaskForm):
    status = BooleanField("Down Status", validators=[DataRequired()])
    submit = SubmitField("Submit")

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DiningFeedbackForm(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CourseFeedbackForm(FlaskForm):
    abbreviation = StringField("Abbreviation", validators=[DataRequired()])
    course = StringField("Course", validators=[DataRequired()])
    department = SelectField("Department", choices = tuples, validators=[DataRequired()])
    professor = StringField("Professor", validators = [DataRequired()])
    semester = SelectField("Semester", choices = [("Fall 2018", "Fall 2018"), ("Spring 2019", "Spring 2019"), \
        ("Summer 2019", "Summer 2019"), ("Fall 2019", "Fall 2019"), ("Spring 2020", "Spring 2020"), ("Summer 2020", "Summer 2020"), \
        ("Fall 2020", "Fall 2020"), ("Spring 2021", "Spring 2021"), ("Summer 2021", "Summer 2021"), \
        ("Fall 2021", "Fall 2021"), ("Spring 2022", "Spring 2022"), ("Summer 2022", "Summer 2022"), \
        ("Fall 2022", "Fall 2022")])
    rating = RadioField("Rating", choices = [('1', '1'), ('2', '2'), \
        ('3', '3'), ('4', '4'), ('5', '5')])
    difficulty = RadioField("Difficulty", choices = [('1', '1'), ('2', '2'), \
        ('3', '3'), ('4', '4'), ('5', '5')])   
    usefulness = RadioField("Usefulness", choices = [('1', '1'), ('2', '2'), \
        ('3', '3'), ('4', '4'), ('5', '5')]) 
    online = RadioField("Online", choices = [('y', 'Yes'), ('n', 'No')])
    credit = RadioField("Credit", choices = [('y', 'Yes'), ('n', 'No')])
    textbook = RadioField("Textbook", choices = [('y', 'Yes'), ('n', 'No')])
    attendance = RadioField("Attendance", choices = [('y', 'Yes'), ('n', 'No')])
    grade = SelectField("Grade", choices = [("A+", 'A+'), ('A', 'A'), \
        ('A-','A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), \
        ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('E', 'E')])
    review = TextAreaField("Review", widget = TextArea())
    submit = SubmitField("Submit",)

class HomeForm(FlaskForm):
    department = SelectField("Department", choices = tuples, validators=[DataRequired()])
    abbreviation = StringField("Abbreviation", validators=[DataRequired()])
    submit = SubmitField("Submit",)

class RateThisForm(FlaskForm):
    submit = SubmitField("Submit")

