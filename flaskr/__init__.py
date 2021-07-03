# Python Dependencies
import os
import sys

# Exsternal Dependencies
from flask import Flask

# Local Dependencies
from app import bp


def return_path() -> str:
	""" Returns the root file path """
	path = os.path.dirname(os.path.dirname(__file__))
	return path


def create_app():
	""" Creates the flask app from blueprint """
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app
