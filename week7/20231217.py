import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate('2023AutumnProject/fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json')

firebase_admin.initialize_app(cred)

db=firestore.client()

'''doc={'name':'Harrison',
     'email':'bagelcatboy@gmail.com'
     }
doc_ref=db.collection('Autumn2023_Students').document('student01')
doc_ref.set(doc)
collection_ref=db.collection('Autumn2023_Students')
collection_ref.add(doc)
'''
s02={'name':'Jaclyn',
     'email':'jaclyn@gmail.com'
     }
s02_ref=db.collection('Autumn2023_Students').document('student02')
s02_ref.set(s02)
path='Autumn2023_Students/student01'

doc_ref=db.document(path)
try:
    doc=doc_ref.get()
    doc_dict=doc.to_dict()
    print('The contentof the document is:{}'.format(doc_dict))
except:
    print("The reference of document does not exist, please check the path is correct or not{}".format(path)) 
path='Autumn2023_Students'
collection_ref=db.collection(path)
docs=collection_ref.where('name','==','Jaclyn').get()
'''for doc in docs:
    print("The content of document is {}".format(doc.to_dict()))'''
path='Autumn2023_Students/student01'
doc_ref=db.document(path)
doc={'birthday':'1101'}
doc_ref.update(doc)
doc_ref=db.document(path)
contacts={'email':'bagelcatboy@gmail.com','phone':'0910123456'}
doc={'contacts':contacts}
doc_ref.update(doc)
path='Autumn2023_Students/student02'
doc_ref=db.document(path)
doc_ref.delete()
student_ref=db.collection('Autumn2023_Students')
docs=student_ref.get()
for doc in docs:
    doc.reference.delete()
