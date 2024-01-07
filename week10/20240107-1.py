import pyrebase
import os
import firebase_admin
from firebase_admin import credentials, storage


cred=credentials.Certificate("../fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-5e7d6.appspot.com'})

bucket = storage.bucket()
dir_path = "./Firebase_project3/image"
filelist = [f for f in os.listdir(dir_path) if f.endswith("png")]

for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "project_images/"+file
    print("Now is uploading file {}.".format(file_path))
    blob=bucket.blob(blob_path)
    blob.upload_from_filename(file_path)


'''import pyrebase
import os

config= {
  "apiKey": "AIzaSyCyAHFBC50HzoqBMSzCPKxSYt_whaqUy8w",
  "authDomain": "fir-test-5e7d6.firebaseapp.com",
  "projectId": "fir-test-5e7d6",
  "storageBucket": "fir-test-5e7d6.appspot.com",
  "messagingSenderId": "717063514473",
  "appId": "1:717063514473:web:e3e1046f010ac91d2b75f8",
  "databaseURL":"",
  "serviceAccount":"../fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json"
  }

#connect firebase and the python script by using app config.
firebase=pyrebase.initialize_app(config)
#get a reference to the auth service
auth=firebase.auth()

dir_name='project_images'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

storage=firebase.storage()
all_files=storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)'''





