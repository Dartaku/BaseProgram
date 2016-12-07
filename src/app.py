from src.common.database import Database
from flask import Flask, render_template
from src.models.users.views import user_blueprint

__author__ = 'Dartaku'


app = Flask(__name__) #'__main__'
app.config.from_object('config')
app.secret_key='Dartaku'


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(user_blueprint, url_prefix="/users")