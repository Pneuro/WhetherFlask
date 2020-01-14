from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'c822c2bd2a140e8ea1da0d5c5246b990'
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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
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
