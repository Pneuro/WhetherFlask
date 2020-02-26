from flask import Flask, render_template, url_for, flash, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import ContactForm
import os
import sys
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


app = Flask(__name__)
db = SQLAlchemy(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'koncept999@gmail.com'
app.config["MAIL_PASSWORD"] = '00iiccuu881122'


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
test = ['dancing', 'purple', 'guitar']
posts = [{
    "_id": 0,
    'title': 'Pondering',
    'author': 'Sammie Kendrick',
    'entry': "For matters of existance, wouldn't we all benefit from finding a way to do what we love in such a fashion that would make us thrive? As a thinker, perhaps there should be more consideration in my life involving solving complex problems.",
}, {
    "_id": 1,
    'title': 'Secrets',
    'author': 'Sammie Kendrick',
    'entry': "The idea that if we focus on the thoughts of the life we wish we had, perhaps the thingkers in the world may come up with a solution as to procure such a life, but most motherfuckers are dumb as shit and kind of just wish wish wish. but that doesnt really work now dies it>? ",

}
]


### Navigation #############################################


@app.route('/')
@app.route('/home')
def home():

    return render_template('about.html')


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
    if form.validate_on_submit():
        res = form.data
        print(res)
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
