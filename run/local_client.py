# This is where you start the local gui client from.

path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)

if __name__ == '__main__':
	pass