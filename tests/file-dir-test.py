#TODO: Delete this later for now it's useful to copy and paste from.

print(__file__)
path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'

print(path)