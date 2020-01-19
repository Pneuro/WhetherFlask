from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
import pymongo
from pymongo import MongoClient
import os
import sys
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from selenium import webdriver


app = Flask(__name__)
# cluster = MongoClient(
#     'mongodb+srv://pneuro:--@koncept-database-etudy.gcp.mongodb.net/test')
# db = cluster[""]
# collection = db["data"]

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
test = ['dancing', 'purple', 'guitar']
posts = [{
    "_id": 0, 'title': 'post_1', 'author': 'Sammie Kendrick', 'email': 'thedylankendrick@gmail.com',
}
]


######################################Navigation##################################################


@app.route('/')
@app.route('/home')
def home():
    return render_template('about.html', )


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.email.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route('/login')
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('about'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


@app.route('/softeng')
def softeng():
    return render_template('softeng.html', title='Software Engineering')


@app.route('/Music')
def music():
    return render_template('music.html', title='Music')

###### Scraping Import ###########################################################################
# UNIVERSAL AUDIO APOLLO TWIN X DUO THUNDERBOLT 3 INTERFACE


url = 'https://www.musiciansfriend.com/pro-audio/universal-audio-apollo-twin-x-duo-thunderbolt-3-audio-interface/l69012000000000?rNtt=apollo&index=1'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
title = page_soup.find('title')
containers = page_soup.find('span', 'price-wrap')
clean = containers.text.strip()
cleanTitle = title.text.strip()
displayRes = 'The ' + cleanTitle + ' is going currently ' + str(clean)
apollo = ('The ' + cleanTitle + ' is going to cost ' + str(clean))

# MARSHALL JVM SERIES JVM410H 100W TUBE GUITAR AMPLIFIER


urlAmp = 'https://www.musiciansfriend.com/amplifiers-effects/marshall-jvm-series-jvm410h-100w-tube-guitar-amp-head'
reqAmp = Request(urlAmp, headers={'User-Agent': 'Mozilla/5.0'})
webpageAmp = urlopen(reqAmp).read()
page_soup_Amp = soup(webpageAmp, "html.parser")
titleAmp = page_soup_Amp.find('title')
containersAmp = page_soup_Amp.find('span', 'price-wrap')
cleanAmp = containersAmp.text.strip()
cleanTitleAmp = titleAmp.text.strip()
displayResAmp = 'The ' + cleanTitleAmp + \
    ' is going to cost ' + str(cleanAmp)
amp = ('The ' + cleanTitleAmp + ' will cost ' + cleanAmp)

# Apple Watch

urlWatch = 'https://www.amazon.com/Apple-Watch-GPS-40mm-Aluminum/dp/B07XR5TRSZ/ref=sr_1_2_sspa?keywords=apple+watch&qid=1578007379&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQ0FGVjRKQzY1TDBTJmVuY3J5cHRlZElkPUEwOTU0ODg4M0lBT1ZFVkZMSlQ1MyZlbmNyeXB0ZWRBZElkPUEwMDg1NjAwMU5aSVFQNEtORTc0MSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
reqWatch = Request(urlWatch, headers={'User-Agent': 'Mozilla/5.0'})
webpageWatch = urlopen(reqWatch).read()
page_soup_Watch = soup(webpageWatch, "html.parser")
titleWatch = page_soup_Watch.find('title')
containersWatch = page_soup_Watch.find(
    'span', 'priceBlockBuyingPriceString')
cleanWatch = containersWatch.text.strip()
cleanTitleWatch = titleWatch.text.strip()
displayResWatch = 'The ' + cleanTitleWatch + \
    ' is going to cost ' + str(cleanWatch)
watch = ('The ' + cleanTitleWatch + ' in question will cost ' + cleanWatch)

# Blog Attempt

urlWatch = 'https://planetpython.org/'
reqWatch = Request(urlWatch, headers={'User-Agent': 'Mozilla/5.0'})
webpageWatch = urlopen(reqWatch).read()
page_soup_Watch = soup(webpageWatch, "html.parser")
titleWatch = page_soup_Watch.find('title')
containersWatch = page_soup_Watch.find_all('h3', 'post')
containersWatch = page_soup_Watch.find('h4', '')
cleanWatch = containersWatch.text.strip()
cleanTitleWatch = titleWatch.text.strip()
displayResWatch = 'The ' + cleanTitleWatch + \
    ' is going to cost ' + str(cleanWatch)
blog = (cleanTitleWatch, cleanWatch)
results = [apollo, amp, watch, blog]


@app.route('/blog')
def blog(): return render_template(
    'blog.html', title='Blog', results=results, posts=posts)


@app.route('/Contact')
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == "__main__":
    app.run()
