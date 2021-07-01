# Returns root file path
def return_path()
	path = ''
	for folder in __file__.split('/'):
		path = path + folder
		if folder == 'open-pos':
			break
		else:
			path = path + '/'
	return path