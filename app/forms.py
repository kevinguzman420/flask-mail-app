from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RestorePassForm(FlaskForm):
    password = PasswordField('Enter the new password', validators=[
                                                                    DataRequired(message="Enter a password."),
                                                                    EqualTo('confirm', message="Passwords must match")
                                                                    ])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(message="Enter a password.")])
    submit = SubmitField('Change')

class RestorePassMailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Input an email"), Email(message="Input an valid email.")])
    submit = SubmitField('Send email')