# Create the app for the flask server
import sys

from flask import Flask

path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

from flaskr.app import bp

def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app