# Returns database config.
def get_config(database_name, warnings=True) -> dict:
	"""
	Returns a my SQL database config

	Formats a config dictionary for use in mysql.connector functions.

	Parameters:
	database_name (str) -- The name of the database you wish to connect to.
	warnings (bool) -- Decides if mysql.connector.connect() will raise on warnings. (defaults to True, implying that it will raise on warnings.)

	Returns:
	dict : A dictionary that can be put into mysql.connector.connect()
	"""

	config = {
		'user': 'none',
		'password': 'none',
		'host': '127.0.0.1',
		'database': database_name,
		'raise_on_warnings': warnings
		}

	return config