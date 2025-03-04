# if sys.version_info.major == 3 and sys.version_info.minor >= 10:
#     pass
import pyrebase #NOTE: Pyrebase4 to fix collections 3.10 module errors

import firebase_admin
from firebase_admin import credentials, auth,storage,\
    firestore as adminsdk_firestore

from google.cloud import firestore

from functools import wraps,reduce,lru_cache
import json

import requests

import dotenv
import os

from config import DATABASES_ENV_FILE_NAME,Chosen_EnumDatabase_Conn_Obj_,ApplicationSessionConfig

FIREBASE_CONFIG_JSON_NAME = ".firebase_config.json"
FIREBASE_ADMINSDK_CREDS_SERVICEKEYS_FILENAME = ".credentials_firebase_adminsdk_n0xv8_cd14a39876.json"

dotenv.load_dotenv(DATABASES_ENV_FILE_NAME)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FIREBASE_ADMINSDK_CREDS_SERVICEKEYS_FILENAME

firebase_sdkadmin = firebase_admin.initialize_app()

fb_config = json.load(open(FIREBASE_CONFIG_JSON_NAME))
fb_config.setdefault('databaseURL',
                     Chosen_EnumDatabase_Conn_Obj_.SELF.databaseServerURL  #NOTE: Current database is chosen here
                     )
fb_config.setdefault('storageBucket',os.environ['FIREBASE_STORAGE_BUCKET'])

fb_adminsdk_cred = credentials.Certificate(FIREBASE_ADMINSDK_CREDS_SERVICEKEYS_FILENAME)


firebase_default_app = firebase_admin.initialize_app(fb_adminsdk_cred,
                                                     {'storageBucket': os.environ['FIREBASE_STORAGE_BUCKET']},
                                                     name="adminsdk_firebase")

_firebase = pyrebase.initialize_app(fb_config)
_auth = _firebase.auth()#Pyrebase4 api,: send_email_verification, send_password_reset_email, etc..
fb_db = _firebase.database()
fb_storage = _firebase.storage()

mainStorageBucket = storage.bucket(name=os.environ['FIREBASE_STORAGE_BUCKET'])

firestore_db = adminsdk_firestore.client()

# def authenticate_user(email="", password=""):
    # user = auth.get_user_by_email(email)
    # print(vars(user))
    #
    #
    # uid = "HxlC0GZ2wuYHm7QRTXmE9GUDn402"
    # custom_claims = {"admin": True}  # Optional custom claims
    #
    # strtoken = _auth.create_custom_token(uid,custom_claims,1)
    # signedIn_user = _auth.sign_in_with_custom_token(strtoken)
    # print(strtoken)
    # # signedIn_user = _auth.sign_in_with_email_and_password(email, password)
    # print(signedIn_user)
    #
    # print(_auth.get_account_info(signedIn_user))

    # Generate an ID token
    # id_token_encoded : bytes = auth.create_custom_token(uid, custom_claims)
    # id_token : str = id_token_encoded.decode("utf-8")
    #
    # pyrebaseUserRecord = _auth.get_account_info(id_token)
    # print(json.dumps(pyrebaseUserRecord))
    # print(pyrebaseUserRecord)
    # print(dict(**pyrebaseUserRecord))
    # print(auth.verify_id_token(id_token_encoded))
    # Generate a refresh token
    # refresh_token = auth.generate_refresh_token(uid)
    ##  print(_auth.refresh(refresh_token))


    # #auth.create_session_cookie()
    # #print(auth.verify_session_cookie())

    # return None
    # return id_token, refresh_token

if __name__ == '__main__':
    doc_ref = firestore_db.collection(u'test_users').document(u'datafile1')
    doc_ref.set({
        'field1': 324234.242,
        'field2' : "something"
    })

    # print(fb_db.__repr__())
    # data = {
    #         u'firebaseUUID': u'99asdjN32489hsdub*adn',
    #         u'userType': 'EMPLOYER'
    #     }
    #
    # fb_db.child("users_extra_info").child("AntoineCantin").set(data)
    # print(fb_db.child("users_extra_info").get().val())
    # users_ref = firestore_db.collection(u'users')
    # doc_ref = users_ref.document(u'antoinecantin')
    # doc_ref.set(data
    # )
    #print(doc_ref)


    # SIGNIN_INFO = dict(
    #     email = "test@hotmail.com",
    # password = "abc123"
    # )
    # user = None
    # try:
    #     user = _auth.create_user_with_email_and_password(
    #         **SIGNIN_INFO
    #     )
    #
    # except requests.exceptions.HTTPError as err:
    #     #NOTE: print(err.strerror)
    #     user = _auth.sign_in_with_email_and_password(
    #         **SIGNIN_INFO
    #     )
    # else:
    #     print("Created new user! ")
    #
    # info = _auth.get_account_info(user['idToken'])
    #
    # print(*user.items(),sep="\n",end="\n\n\r")

