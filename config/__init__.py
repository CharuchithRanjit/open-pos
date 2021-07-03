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
	Returns the correct path for local dependencies.

	Gets the current file path, then loops up two files and finally adds open-pos file path to the end.

	Parameters:
	None

	Returns:
	str : The root file path
	"""

	path = os.path.dirname(os.path.dirname(__file__))
	return path