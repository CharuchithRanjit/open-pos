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
from flaskr.auth import *


bp = Blueprint("app", __name__)


@bp.route('/')
def index() -> object:
	file_path = url_for('templates/main', filename='index.html')
	render = lambda : render_tempate(file_path)
	return render()


@bp.route('/signin')
def signin() -> object:
	file_path = url_for('templates/auth', filename='signin.html')
	render = lambda : render_template(file_path)
	return render()


@bp.route('/signup')
def signup() -> object:
	file_path = url_for('templates/auth', filename='signup.html')
	render = lambda : render_template(file_path)
	return render()


@bp.route('/signout')
def signout() -> object:
	file_path = url_for('templates/auth', filename='signout.html')
	render = lamda : redner_template(file_path)
	return render()



