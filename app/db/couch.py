import couchdb
from app.config import COUCHDB_URL

def get_couchdb_server():
    return couchdb.Server(COUCHDB_URL)
