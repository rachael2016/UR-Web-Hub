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
        "Sustainability Studies", "Theater", "Visual and Cultural Studies", "Writing"]
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

class CourseFeedbackForm(FlaskForm):
    abbreviation = StringField("Abbreviation", validators=[DataRequired()])
    course = StringField("Course", validators=[DataRequired()])
    department = SelectField("Department", choices = tuples, validators=[DataRequired()])
    professor = StringField("Professor", validators = [DataRequired()])
    rating = RadioField("Rating", choices = [('one', '1'), ('two', '2'), \
        ('three', '3'), ('four', '4'), ('five', '5')])
    difficulty = RadioField("Difficulty", choices = [('one', '1'), ('two', '2'), \
        ('three', '3'), ('four', '4'), ('five', '5')])   
    usefulness = RadioField("Usefulness", choices = [('one', '1'), ('two', '2'), \
        ('three', '3'), ('four', '4'), ('five', '5')]) 
    online = RadioField("Online", choices = [('y', 'Yes'), ('n', 'No')])
    credit = RadioField("Credit", choices = [('y', 'Yes'), ('n', 'No')])
    textbook = RadioField("Textbook", choices = [('y', 'Yes'), ('n', 'No')])
    attendance = RadioField("Attendance", choices = [('y', 'Yes'), ('n', 'No')])
    grade = SelectField("Grade", choices = [("A+", 'A+'), ('A', 'A')])
    review = TextAreaField("Review", widget = TextArea())
    submit = SubmitField("Submit",)

class HomeForm(FlaskForm):
    department = SelectField("Department", choices = tuples, validators=[DataRequired()])
    abbreviation = StringField("Abbreviation", validators=[DataRequired()])
    submit = SubmitField("Submit",)




