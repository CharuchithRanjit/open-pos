# Python Dependencies
import sys

path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

from local_register.main import *

if __name__ == '__main__':
	pass