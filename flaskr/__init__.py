# Create the app for the flask server
from flask import Flask

from flakr.app import bp

def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app