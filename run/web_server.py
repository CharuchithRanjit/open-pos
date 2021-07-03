""" Starts the web server """

# Python Dependencies
import os
import sys

# Exsternal Dependencies
from flask import Flask

# Set File Path To Root
path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(1, path)

# Local Dependencies
from flaskr.__init__ import create_app


if __name__ == "__main__":
	app = create_app()
	app.run()
