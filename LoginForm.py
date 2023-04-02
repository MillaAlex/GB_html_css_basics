from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class Lf(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Pass", validators=[DataRequired()])
    password_again = PasswordField("Repeat pass", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Register")
    