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
path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

from flaskr.auth import user_check
from flaskr.auth import user_signup
from flaskr.auth import admin_check
from flaskr.auth import admin_signup

bp = Blueprint("app", __name__)


@bp.route('/')
def index() -> object:
	file_path = 'main/index.html'
	render = lambda : render_template(file_path)
	return render()


@bp.route('/auth/user/signin')
def user_signin() -> object:
	file_path = 'auth/user/signin.html'
	render = lambda : render_template(file_path)
	return render()


@bp.route('/auth/admin/signin')
def admin_signin() -> object:
	file_path = 'auth/admin/signin.html'
	render = lambda : render_template(file_path)
	return render()


@bp.route('/user/home')
def user_home() -> object:
	file_path = 'user/home.html'
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


@bp.route('/user/schedule')
def user_schedule() -> object:
	file_path = 'templates/user/schedule.html'
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


@bp.route('/user/hours')
def user_hours() -> object:
	file_path = 'templates/user/hours.html'
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


@bp.route('/user/help')
def user_help() -> object:
	file_path = 'templates/user/help.html'
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


@bp.route('/user/settings')
def user_settings() -> object:
	file_path = 'templates/user/settings.html'
	render = lambda : render_template(file_path)
	if user_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


@bp.route('/user/signout')
def user_signout() -> object:
	file_path = 'templates/user/signout.html'
	render = lambda : render_template(file_path)
	pass


@bp.route('/admin/home')
def admin_home() -> object:
	file_path = 'templates/admin/home.html'
	render = lambda : render_template(file_path)
	if admin_check(session['username'], session['password']):
		return render()
	else:
		redirect('/')


