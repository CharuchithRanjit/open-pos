# Python Dependencies
import sys

# Exsternal Dependencies
from flask import Flask

# Returns root file path
from app import bp


# Returns root file path.
def return_path()
	path = ''
	for folder in __file__.split('/'):
		path = path + folder
		if folder == 'open-pos':
			break
		else:
			path = path + '/'
	return path


# Creates the flask app.
def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app