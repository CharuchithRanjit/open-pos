""" Starts the gui client. """

# Python Dependencies
import os
import sys

# Exsternal Dependencies
None

# Set File Path To Root
path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(1, path)

# Local Dependencies
from local_client.main import *


if __name__ == '__main__':
	pass
