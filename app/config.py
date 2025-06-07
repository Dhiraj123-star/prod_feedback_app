import os
from dotenv import load_dotenv

load_dotenv()

COUCHDB_USER = os.getenv("COUCHDB_USER")
COUCHDB_PASSWORD = os.getenv("COUCHDB_PASSWORD")
COUCHDB_URL = os.getenv("COUCHDB_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
