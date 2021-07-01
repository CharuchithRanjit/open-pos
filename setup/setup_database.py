# Exsternal Dependencies
import mysql.connector
from mysql.connector import errorcode

# Python Dependencies
import sys

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())
from config.db_config import get_config

def connect_database():
	try:
		cnx = mysql.connector.connect(**get_config())
		return cnx

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print('Something is wrong with your username or password.')

		elif err.erno == errorcode.ER_BAD_DB_ERROR:
			print('Database does not exsist.')

		else:
			print(err)
			exit(1)

	else:
		cnx.close()


def create_database(database_name):
	cursor = connect_database()
	cursor = cnx.cursor()

	try:
		cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)
	else:
		print(err)
		exit(1)

	try:
		cursor.execute("USE {}").format(database_name)
		print('Database {} has been created'.format(database_name))
	except mysql.connector.Error as err:
		print("Database {} does not exsit.".format(database_name))
	else:
		print(err)
		exit(1)

	cursor.close()
	cnx.close()



def create_table(database_name, table_name):
	cnx = connect_database()
	cursor = cnx.cursor()
	try:
		cursor.execute(table_name)

	except mysql.connector.Error as err:
		if err.erno == errorcode.ER_TABLE_EXISTS_ERROR:
			print('Table {} already exsists.'.format(table_name))

		else:
			print(err.msg)

	else:
		print("Table {} has been created.".format(table_name))

	cursor.close()
	cnx.close()










