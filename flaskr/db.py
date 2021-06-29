# Handles all the database stuff
path = ''
for folder in __file__.split('/'):
	path = path + folder
	if folder == 'open-pos':
		break
	else:
		path = path + '/'
sys.path.insert(1, path)


def write_user(username, salt, key, firstname, lastname, dob, perms) -> bool:
	pass


def get_salt(username) -> int:
	pass


def check_key(username, key) -> bool:
	pass