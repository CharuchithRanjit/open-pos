"""
For interacting with users in the database

Classes:
User

Functions:
None

Misc variables:
DATABASE_KEY (str) -- The key for the database
DATABASE_PASSWORD (str) -- The password for the database
DATABASE_URL (str) -- The url for the database
"""

# Python Dependencies
import sys
import os

# Exsternal Dependencies
from supabase_py import create_client
from supabase_py import Client

# Set file path to root
from __init__ import return_path
sys.path.insert(1, return_path())

# Local Dependencies
from config.dotenv import DATABASE_KEY
from config.dotenv import DATABASE_PASSWORD
from config.dotenv import DATABASE_URL


class User:
	"""
	Description:
	A class that allows interaction with users in the database

	Attributes:
	db (object) -- References the supabase database

	Methods:
	create_user(email, password) -- Creates a new user
	auth_user(email, password) -- Checks if login is valid
	"""


	def __init__(self) -> None:
		"""
		Creates a new database object from supabase

		Parameters:
		None

		Returns:
		None
		"""
		self.db = create_client(DATABASE_URL, DATABASE_KEY)


	def create_user(self, email, password):
		"""
		Creates a new user

		Parameters:
		email (str) -- Email for new user
		password (str) -- Password for new user
		"""
		pass


	def auth_user(self, email, password):
		"""
		Authenticates user

		Parameters:
		email (str) -- Email for user
		password (str) -- Password for user
		"""
		user = self.db.auth.signin(email=email password=password)
		return user







