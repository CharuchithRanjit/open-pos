print(__file__)
path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
print(path)