import os
import dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dotenv.load_dotenv()

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv('FIREBASE_PROJECT_ID'),
    "private_key": os.getenv('FIREBASE_PRIVATE_KEY'),
    "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
    "token_uri": os.getenv('FIREBASE_TOKEN_URI'),
})
firebase_admin.initialize_app(cred)

db = firestore.client()