# Tests for the web database
path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

from flaskr.db import *


def read_public():
	pass


def read_private():
	pass


def read_permission():
	pass


def read_no_permission():
	pass


def write_public():
	pass


def write_private():
	pass


def write_permission():
	pass


def write_no_permission():
	pass