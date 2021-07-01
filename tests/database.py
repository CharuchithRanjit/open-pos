# Python Dependencies
import sys

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())

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