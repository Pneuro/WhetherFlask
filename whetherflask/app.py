from flask import Flask, render_template, url_for, flash, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import ContactForm
import os
import sys
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import smtplib
from secrets import password
import weather

app = Flask(__name__)
db = SQLAlchemy(app)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'koncept999@gmail.com'
app.config["MAIL_PASSWORD"] = '/'


### Secret Key ##########################################
app.config.update(

    # Set the secret key to a sufficiently random value
    SECRET_KEY=os.urandom(24),

    # Set the session cookie to be secure
    SESSION_COOKIE_SECURE=True,

    # Set the session cookie for our app to a unique name
    SESSION_COOKIE_NAME='Portfolio-WebSession',

    # Set CSRF tokens to be valid for the duration of the session. This assumes you’re using WTF-CSRF protection
    WTF_CSRF_TIME_LIMIT=None

)


def sendemails():
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('koncept999@gmail.com', password)
    conn.sendmail('koncept999@gmail.com',
                  'thedylankendrick@gmail.com', f'')
    conn.quit()


weather_display = weather.datacoll


### Navigation #############################################


@app.route('/')
@app.route('/home')
def home():

    return render_template('about.html', name="About", weather_display=weather_display)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.email.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


@app.route('/intps')
def login():
    return render_template('login.html', title='INTP')


@app.route('/softeng')
def softeng():
    return render_template('softeng.html', title='Software Engineering')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if request.method == "POST":

        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login('koncept999@gmail.com', password)
        conn.sendmail('koncept999@gmail.com',
                      'thedylankendrick@gmail.com', f'Data sent from FLASK - \nName: {form.name.data} \nEmail: {form.email.data}\nBody: {form.body.data}\nEmployer?: {form.employer.data}')
        conn.quit()
        return render_template('thanks.html')

    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
