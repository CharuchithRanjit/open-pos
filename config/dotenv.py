"""
Loads dotenv variables

Classes:
None

Functions:
None

Misc variables:
DATABASE_KEY (str) -- The key for the database
DATABASE_PASSWORD (str) -- The password for the database
DATABASE_URL (str) -- The url for the database
"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DATABASE_KEY = os.environ.get("DATABASE_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_URL = os.environ.get("SUPABASE_URL")