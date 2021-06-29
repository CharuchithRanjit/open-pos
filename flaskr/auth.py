# Handles all of the authentication stuff
import hashlib
import os

from flask.db import write_user
from flask.db import get_salt
from flask.db import check_key


def user_signup(username, password, firstname, lastname, dob) -> list:
	salt = os.urandom(32)
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	perms = 0
	write_user(username, salt, key, firstname, lastname, dob, perms)


def user_check(username, password) -> bool:
	salt = get_salt(username)
	key = hashlib.pdkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	if check_key(username, key):
		return True
	else:
		return False