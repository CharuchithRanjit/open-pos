__author__ = "Jadon Zufall"
__copyright__ = "Copyright 2021, Amphetamines"
__credits__ = ["Jadon Zufall"]
__license__ = "MIT"
__version__ = "dev_non_functional"
__maintainer__ = "Jadon Zufall"
__email__ = "jadonzufall@gmail.com"
__status__ = "non_functional"

# Python Dependencies
import sys

# Exsternal Dependencies
from flask import Flask

path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

from flaskr.__init__ import create_app

if __name__ == "__main__":
	app = create_app()
	app.run()