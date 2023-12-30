import firebase_admin
from firebase_admin import credentials, storage
cred=credentials.Certificate("../fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-5e7d6.appspot.com'})

file_path="Firebase_project/image/bed1.jpg"
bucket=storage.bucket()
blob=bucket.blob(file_path)
blob.upload_from_filename(file_path)
