"""
Filename : app.py
Description : Returns web pages to display.
"""

# Python Dependencies
import sys

# Dependencies
from flask import Flask
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session

# Local Dependencies
sys.path.insert(1, '/Users/jadon/Python/open-pos')
from flaskr.auth import user_check
from flaskr.auth import user_signup

bp = Blueprint("app", __name__)

"""
---------------------------
--- Public facing pages ---
---------------------------
"""

# STATIC PAGE
@bp.route('/')
def index() -> object:
	file_path = 'main/index.html'
	render = lambda : render_template(file_path)
	return render()


# DYNAMIC PAGE
@bp.route('/signin')
def signin() -> object:
	file_path = url_for('templates/auth', filename='signin.html')
	render = lambda : render_template(file_path)
	return render()


# DYNAMIC PAGE
@bp.route('/signup')
def signup() -> object:
	file_path = url_for('templates/auth', filename='signup.html')
	render = lambda : render_template(file_path)
	return render()


"""
-------------------------
--- User facing pages ---
-------------------------
"""

# DYNAMIC PAGE
@bp.route('/user/home')
def user_home() -> object:
	file_path = url_for('templates/user', filename='home.html')
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


# DYNAMIC PAGE
@bp.route('/user/schedule')
def user_schedule() -> object:
	file_path = url_for('templates/user', filename='schedule.html')
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


# DYNAMIC PAGE
@bp.route('/user/hours')
def user_hours() -> object:
	file_path = url_for('templates/user', filename='hours.html')
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


# DYNAMIC PAGE
@bp.route('/user/help')
def user_help() -> object:
	file_path = url_for('templates/user', filename='help.html')
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


# DYNAMIC PAGE
@bp.route('/user/settings')
def user_settings() -> object:
	file_path = url_for('templates/user', filename='settings.html')
	render = lambda : render_template(file_path)
	pass


# DYNAMIC PAGE
@bp.route('/user/signout')
def user_signout() -> object:
	file_path = url_for('templates/user', filename='signout.html')
	render = lambda : render_template(file_path)
	pass


"""
--------------------------
--- Admin facing pages ---
--------------------------
"""

# DYNAMIC PAGE
@bp.route('/admin/home')
def admin_home() -> object:
	file_path = url_for('templates/admin', filename='home.html')
	render = lambda : render_template(file_path)
	return render()


