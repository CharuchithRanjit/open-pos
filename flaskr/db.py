#TODO: Delete this file

# Python Dependencies
import sys

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())


def write_user(username, salt, key, firstname, lastname, dob, perms) -> bool:
	pass


def get_user_salt(username) -> int:
	pass


def check_user_key(username, key) -> bool:
	pass


def write_admin(username, salt, key) -> bool:
	pass


def get_admin_salt(username) -> int:
	pass


def check_admin_key(username, key) -> bool:
	pass


def user_clock_in(username) -> None:
	pass


def user_clock_out(username) -> None:
	pass


def write_user_pref(username, pref) -> None:
	pass


def read_user_pref(username, pref) -> None:
	pass


def write_admin_pref(username, pref) -> None:
	pass


def read_admin_pref(username, pref) -> None:
	pass

