# Python Dependencies
import sys

# Exsternal Dependencies
import mysql.connector
from mysql.connector import errorcode

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())
from config.db_config import get_config


def connect() -> None:
	return mysql.connector.connect(**get_config())


def write_user() -> None:
	try:
		cnx = mysql.connector.connect(**get_config())

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print('Something is wrong with your username or password.')

		elif err.erno == errorcode.ER_BAD_DB_ERROR:
			print('Database does not exsist.')

		else:
			print(err)

	else:
		cnx.close()