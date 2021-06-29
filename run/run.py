# This is where you start the webserver from

from flask import Flask
from flakr.__init__ import create_app

if __name__ == "__main__":
	app = create_app()
	app.run()