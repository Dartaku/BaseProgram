from src.common.database import Database
from flask import Flask, render_template


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

from src.models.users.views import user_blueprint
from src.models.products.views import products_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(products_blueprint, url_prefix="/products")