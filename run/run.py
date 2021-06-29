# This is where you start the webserver from
import sys

from flask import Flask

sys.path.insert(1, '/Users/jadon/Python/open-pos')
from flaskr.__init__ import create_app

if __name__ == "__main__":
	app = create_app()
	app.run()