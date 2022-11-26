from wtforms import BooleanField, SubmitField, ValidationError
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo, DataRequired, Length

class UserReport(FlaskForm):
    status = BooleanField("Down Status", validators=[DataRequired()])
    submit = SubmitField("Submit")