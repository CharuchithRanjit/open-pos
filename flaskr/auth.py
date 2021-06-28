# Handles all of the authentication stuff
from flaskr.db import get_db


def signin(email, password):
	pass


def signup(email, password1, password2, firstname, lastname, dob):
	if password1 != password2:
		return({'TYPE' : 'ERROR', 'MISC' : 'Password fields did not match.'})



def signout():
	pass


def auth_check(email, hash):
	pass