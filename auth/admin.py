"""
For interacting with admins in the database

Classes:
Admin

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


class Admin():
	"""
	Description:
	A class that allows for interaction with admins in the database.

	Attributes:
	None

	Methods:
	None
	"""


	def __init__(self):
		pass