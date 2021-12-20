from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class MarketingMailForm(FlaskForm):
    template_name = StringField('Email Name', validators=[DataRequired(message="Input a file name")])
    message = TextAreaField('Message', validators=[DataRequired(message="Input a message.")])
    submitMailMark = SubmitField('SEND MARKETING MAILS')

