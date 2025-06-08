import couchdb
from app.config import COUCHDB_URL, COUCHDB_USER, COUCHDB_PASSWORD
from app.utils.security import hash_password

def get_couchdb_server():


    return couchdb.Server(COUCHDB_URL)

db_name = "users"
server = get_couchdb_server()
if db_name not in server:
    db = server.create(db_name)
else:
    db = server[db_name]

def get_user_by_email(email: str):
    selector = {"email": email}
    result = list(db.find({"selector": selector}))
    if result:
        return result[0]
    return None

def create_user(email: str, password: str):
    hashed_pw = hash_password(password)
    user_doc = {
        "email": email,
        "hashed_password": hashed_pw
    }
    doc_id, doc_rev = db.save(user_doc)
    return {"id": doc_id, "email": email}
