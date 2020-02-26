from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
                       DataRequired("Please enter your name.")])
    email = StringField(label='Email', validators=[
                        DataRequired("Please enter your email."), Email()])
    body = TextAreaField()
    employer = BooleanField(label="Employer?")
    submit = SubmitField('Submit')


class MyBlog(FlaskForm):
    title = StringField(label='Title')
    body = StringField(label='Consideration')
    submit = SubmitField('Submit Entry')
