import firebase_admin
from firebase_admin import credentials, storage
cred=credentials.Certificate("../fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json")
firebase_admin.initialize_app(cred,{'storageBucket':'fir-test-5e7d6.appspot.com'})

'''file_path="Firebase_project/image/bed1.jpg"
bucket=storage.bucket()
blob=bucket.blob(file_path)
blob.upload_from_filename(file_path)
'''

'''bucket=storage.bucket()
def upload_blob(bucket,source_file_name,destination_blob_name):
    blob=bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} upload to {destination_blob_name}.')

upload_blob(bucket,"photo-1503756234508-e32369269deb.webp",'nature/beautiful_sea.webp')'''

'''import os
dir_path="./taipei"
filelist=[f for f in os.listdir(dir_path) if f.endswith('.png')]
print(filelist)
bucket=storage.bucket()
for file in filelist:
    file_path=dir_path+'/'+file
    blob_path='taipei/'+file    
    print('now is uploading file {}.'.format(file_path))
    blob=bucket.blov(blob_path)
    blob.upload_from_filename(file_path)
def upload_blob(bucket,source_file_name,destination_blob_name):
    blob=bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} upload to {destination_blob_name}.')

upload_blob(bucket,"taipei/dolysrwdksfvrisnptnw.jpg",'Taipei/101-1.jpg')
upload_blob(bucket,"taipei/taipei-101-tawain-1200x1694.jpg",'Taipei/101-2.jpg')
upload_blob(bucket,"taipei/Taipei101ObservatoryTicket.jpg",'Taipei/101-3.jpg')'''

bucket=storage.bucket()
blob=bucket.blob('nature/sea.webp')
blob.download_to_filename('my_love1.webp')