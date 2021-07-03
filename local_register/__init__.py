#Python Dependencies
import os

# Exsternal Dependencies
None

# Local Dependencies
None


def return_path() -> str:
	""" Returns the root file path """
	path = os.path.dirname(os.path.dirname(__file__))
	return path