"""
Short Description

Classes:
User

Functions:
None

Misc variables:
DATABASE_KEY (str) -- The key for the database
DATABASE_PASSWORD (str) -- The password for the database
DATABASE_URL (str) -- The url for the database
"""

__author__ = "Jadon Zufall"
__copyright__ = "Copyright 2021, Jadon Zufall"
__credits__ = ["Jadon Zufall"]
__license__ = "MIT"
__version__ = "dev_non_functional"
__maintainer__ = "Jadon Zufall"
__email__ = "jadonzufall@gmail.com"
__status__ = "non_functional"

import os


def return_path() -> str:
	"""
	Returns the root file path for dependencies.

	Parameters:
	None

	Returns:
	str : The root file path
	"""
	path = os.path.dirname(os.path.dirname(__file__))
	return path