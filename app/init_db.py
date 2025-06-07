# app/init_db.py

import os
import requests
from requests.auth import HTTPBasicAuth

COUCHDB_URL = os.getenv("COUCHDB_URL", "http://admin:strongpassword@couchdb:5984")
USER = os.getenv("COUCHDB_USER", "admin")
PASSWORD = os.getenv("COUCHDB_PASSWORD", "strongpassword")

def ensure_users_db_exists():
    db_name = "_users"
    check_url = f"{COUCHDB_URL}/{db_name}"

    try:
        response = requests.get(check_url, auth=HTTPBasicAuth(USER, PASSWORD))
        if response.status_code == 200:
            print(f"✅ '{db_name}' already exists.")
        elif response.status_code == 404:
            print(f"🛠️ '{db_name}' not found. Creating...")
            create_resp = requests.put(check_url, auth=HTTPBasicAuth(USER, PASSWORD))
            if create_resp.status_code == 201:
                print(f"🎉 '{db_name}' created successfully.")
            else:
                print(f"❌ Failed to create '{db_name}': {create_resp.text}")
        else:
            print(f"⚠️ Unexpected response: {response.status_code} -> {response.text}")
    except Exception as e:
        print(f"🔥 Error checking/creating '{db_name}': {e}")

if __name__ == "__main__":
    ensure_users_db_exists()
