from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
from flask_pymongo import Pymongo
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://pneuro:0icu8122>@koncept-database-etudy.gcp.mongodb.net/test'
db = SQLAlchemy(app)
posts = [{
    'id': 'post_1',
    'author': 'Sammie Kendrick',
    'email': 'thedylankendrick@gmail.com',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint dolores expedita odit, vero doloremque aspernatur qui quibusdam non, perferendis magni saepe cum. Consequuntur magni soluta repudiandae iure facilis rem officia.'
},
    {
    'id': 'post_2',
    'author': 'Silent Hearts',
    'email': 'thedylankendrick@gmail.com',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint dolores expedita odit, vero doloremque aspernatur qui quibusdam non, perferendis magni saepe cum. Consequuntur magni soluta repudiandae iure facilis rem officia.'
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
            return redirect(url_for('home'))
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
