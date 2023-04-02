from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class AuthF(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Pass", validators=[DataRequired()])
    submit = SubmitField("Login")
    