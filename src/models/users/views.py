from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.users.user import User
import src.models.users.errors as UserErrors

__author__ = 'Dartaku'


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return render_template("home.html")
        except UserErrors.UserNotExistsError as e:
            return e.message
        except UserErrors.IncorrectPasswordError as e:
            return e.message

    return render_template("users/login.html")  # Send the user an error if their login was invalid


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return render_template("home.html")
        except UserErrors.UserAlreadyRegisteredError as e:
            return e.message
        except UserErrors.InvalidEmailError as e:
            return e.message

    return render_template("users/register.html")  # Send the user an error if their login was invalid


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page"


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return render_template("home.html")
