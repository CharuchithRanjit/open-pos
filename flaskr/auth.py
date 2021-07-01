# Python Dependencies
import hashlib
import os
import sys

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())
from flaskr.db import write_user
from flaskr.db import get_user_salt
from flaskr.db import check_user_key
from flaskr.db import write_admin
from flaskr.db import get_admin_salt
from flaskr.db import check_admin_key


def user_signup(username, password, firstname, lastname, dob) -> None:
	salt = os.urandom(32)
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	perms = 0
	write_user(username, salt, key, firstname, lastname, dob, perms)


def user_check(username, password) -> bool:
	salt = get_user_salt(username)
	key = hashlib.pdkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	if check_user_key(username, key):
		return True
	else:
		return False


def admin_signup(username, password) -> None:
	salt = os.urandom(32)
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	write_admin(username, salt, key)


def admin_check(username, password) -> bool:
	salt = get_admin_salt()
	key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
	if check_admin_key(username, key):
		return True
	else:
		return False