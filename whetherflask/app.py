from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)
cluster = MongoClient(
    'mongodb+srv://pneuro:0icu8122@koncept-database-etudy.gcp.mongodb.net/test')
db = cluster["data"]
collection = db["data"]

####################################### Secret Key ##########################################
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

posts = [{
    "_id": 0, 'title': 'post_1', 'author': 'Sammie Kendrick', 'email': 'thedylankendrick@gmail.com',
}
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('about.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('about'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/softeng')
def softeng():
    return render_template('softeng.html', title='Software Engineering')


@app.route('/Music')
def music():
    return render_template('music.html', title='Music')


@app.route('/Contact')
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == "__main__":
    app.run(debug=True)
