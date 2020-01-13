from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import soundcloud


#####################################################################################
############################# SoundCloud ############################################
#####################################################################################


# client = soundcloud.Client(client_id='dylan-kendrick-183112710')
# track_url = 'https://soundcloud.com/forss/flickermood'
# embed_info = client.get('/oembed', url=track_url)

# # print the html for the player widget
# print(embed_info['html'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # set to false so it cant be left blank
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('about.html')


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
