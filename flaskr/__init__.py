# Create the app for the flask server
import sys

from flask import Flask

sys.path.insert(1, '/Users/jadon/Python/open-pos')
from flaskr.app import bp

def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app