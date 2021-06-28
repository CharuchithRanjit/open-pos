# The main file flask gets webpages from

from flask import Flask
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flaskr.db import get_db
from flaskr.auth import signin
from flaskr.auth import signup
from flaskr.auth import signout
from flaskr.auth import ses_signin


bp = Blueprint("app", __name__)


# The main login page
@bp.route('/')
def index() -> object:
	file_path = url_for('templates/main', filename='index.html')
	render = lambda : render_tempate(file_path)
	return render()


# The sign in page
@bp.route('/signin')
def signin() -> object:
	file_path = url_for('templates/auth', filename='signin.html')
	render = lambda : render_template(file_path)
	return render()


# The sign up page
@bp.route('/signup')
def signup() -> object:
	file_path = url_for('templates/auth', filename='signup.html')
	render = lambda : render_template(file_path)
	return render()


# The sign out page
@bp.route('/signout')
def signout() -> object:
	file_path = url_for('templates/auth', filename='signout.html')
	render = lambda : redner_template(file_path)
	return render()


# The home page for the user
@bp.route('/user/home')
def user_home() -> object:
	file_path url_for('templates/user', filename='home.html')
	render = lambda : render_template(file_path)
	return render()


# The admin panel
@bp.route('/admin/home')
def admin_home() -> object:
	file_path = url_for('templates/admin', filename='home.html')
	render = lambda : render_template(file_path)
	return render()


