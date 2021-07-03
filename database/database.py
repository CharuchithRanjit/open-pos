# Python Dependencies
import sys
import os

# Exsternal Dependencies
import mysql.connector
from mysql.connector import errorcode
import supabase_py
from supabase_py import create_client
from supabase_py import Client

# Local Dependencies
from __init__ import return_path
sys.path.insert(1, return_path())
from config.settings import DATABASE_KEY
from config.settings import DATABASE_PASSWORD
from config.settings import DATABASE_URL



import os
from supabase_py import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class database:
	def __init__(self):
		self.db = create_client(DATABASE_URL, DATABASE_KEY)

	def create_account(self, email, password):
		pass

	def sign_in(self, email, password):
		user = self.db.auth.signin(email=email password=password)

		


# TODO : This function is currently suseptable to SQL Injection.  Well this is likely not an issue fix later.
def create_database(database_name, num_attempts=1) -> bool:
	""" 
	Creates a new database.

	Using mysql.connector this function takes in a database_name and then creates a database named after that string.

	Parameters:
	database_name (str) -- The desired name for the database you wish to create.
	num_attempts (int) -- The number of times the function will attempt to create the database if past attempts have failed. (the default is 1, which implies that the function will only attempt 1 attempt and then stop if the database could not be created first try.)

	Returns:
	bool : If the function returns True then the database was sucessfully created.
	"""

	for i in range(0, num_attempts):
		try:
			cnx = mysql.connector.connect(**get_config(None))
			cursor = cnx.cursor()
			cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
			print('Database {} has been created.').format(database_name)
			return True

		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print('ERROR on attempt {} / {}: Username, Password in config/database_config.py has invalid permissions.'.format(str(i-1), str(num_attempts)))
				continue

			elif err.erno == errorcode.ER_BAD_DB_ERROR:
				print('ERROR on attempt {} / {}: Database in config/database_config.py does not exsist.'.format(str(i-1), str(num_attempts)))
				continue

		else:
			print("UKNOWN_ERROR on attempt {} / {} : {}".format(str(i-1), str(num_attempts), err))
			continue

		finally:
			if cursor:
				cursor.close()
			if cnx:
				cnx.close()

	return False


# TODO : This function is currently suseptable to SQL Injection.  Well this is likely not an issue fix later.
def create_table(database_name, table_name, table_info, num_attempts=1, delete_if_exsist=True) -> bool:
	"""
	Creates a new table in a database.

	Using mysql.connector this function takes in a database_name and table_name and creates a table named after table_name in database database_name.

	Parameters:
	database_name (str) -- The name of the database you are trying to create a table in.
	table_name (str) -- The desired name for the table you wish to create.
	table_info (list) -- A list that should contain each type of value you want to store in the table [FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20)]
	num_attempts (int) -- The number of times the function will attempt to create the table if past attempts have failed. (the default is 1, which implies that the function will only attempt 1 attempt and then stop if the table could not be created first try.)
	delete_if_exsists (bool) -- Determinds if the table will be deleted if it already exsists. (The default is True, which implies the table will be deleted if it already exsists.)
	
	Returns:
	bool : If the function returns True then the table was succesfully created.
	"""

	for i in range(0, num_attempts):
		try:
			cnx = mysql.connector.connect(**get_config(database_name))
			cursor = cnx.cursor()
			if delete_if_exsists:
				cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
			sql_cmd = 'CREATE TABLE {}('.format(table_name)
			for item in table_info:
				sql_cmd = sql_cmd + table_info
				if int(index(item)) != int(len(table_info) - 1):
					sql_cmd = sql_cmd + ', '
			sql_cmd = sql_cmd + ')'
			print('Executing the following mySQL command,')
			print(sql_cmd)
			cursor.execute(sql_cmd)
			print('{} has been succesfully created.'.format(table_name))
			return True

		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print('ERROR on attempt {} / {}: Username, Password in config/database_config.py has invalid permissions.'.format(str(i-1), str(num_attempts)))
				continue

			elif err.erno == errorcode.ER_BAD_DB_ERROR:
				print('ERROR on attempt {} / {}: Database in config/database_config.py does not exsist.'.format(str(i-1), str(num_attempts)))
				continue

			if err.erno == errorcode.ER_TABLE_EXISTS_ERROR:
				print('ERROR on attempt {} / {}: Table {} already exsists.'.format(str(i-1), str(num_attempts), table_name))
				continue

		else:
			print('UKNOWN_ERROR on attempt {} / {} : {}'.format(str(i-1), str(num_attempts), err))
			continue

		finally:
			if cursor:
				cursor.close()
			if cnx:
				cnx.close()

	return False
