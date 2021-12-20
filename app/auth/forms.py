from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Input an email"), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(message="Input a password")])
    email = StringField('Email', validators=[DataRequired(message="Input an email"), Email(message="Input an valid email.")])
    submit = SubmitField('SignUp')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Input an email"), Email(message="Input an valid email.")])
    password = PasswordField('Password', validators=[DataRequired(message="Input a password")])
    remember_me = BooleanField('Remenber me')
    submit = SubmitField('Login')
