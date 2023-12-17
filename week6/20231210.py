'''import pyrebase
from tkinter import *
config= {
  "apiKey": "AIzaSyCyAHFBC50HzoqBMSzCPKxSYt_whaqUy8w",
  "authDomain": "fir-test-5e7d6.firebaseapp.com",
  "projectId": "fir-test-5e7d6",
  "storageBucket": "fir-test-5e7d6.appspot.com",
  "messagingSenderId": "717063514473",
  "appId": "1:717063514473:web:e3e1046f010ac91d2b75f8",
  "databaseURL":""
  }

#connect firebase and the python script by using app config.
firebase=pyrebase.initialize_app(config)
#get a reference to the auth service
auth=firebase.auth()

#webpage added
root=Tk()


loginlabel=Label(root,text='Login page')
accountlabel=Label(root,text='Account')
passwordlabel=Label(root,text='Password')
resultlabel=Label(root,text='')



accountentry=Entry(root)
passwordentry=Entry(root, show='*')
signupbutton=Button(root,text='Sign up', width=10,command=lambda:addUser(root, accountentry, passwordentry))
loginbutton=Button(root,text='Login',width=10,command=lambda: verifyUser(root,accountentry,passwordentry))


loginlabel.pack(pady=5)
accountlabel.pack(pady=5)
accountentry.pack(pady=5)
passwordlabel.pack(pady=5)
passwordentry.pack(pady=5)
signupbutton.pack(pady=5)
loginbutton.pack(pady=5)
resultlabel.pack(pady=5)





def verifyUser(view, accountentry, passwordentry):
    print(accountentry.get(),passwordentry.get())
    print('Login...')
    account=accountentry.get()
    password=passwordentry.get()
    try:
        user=auth.sign_in_with_email_and_password(account,password)
        print('Successfully Login!')
        resultlabel.config(text='Successfully Login')
    except Exception as e:
        print(f'Login Account Failed...')
        resultlabel['text']='Login Account Failed...'


def addUser(view, accountentry, passwordentry):
    print(accountentry.get(),passwordentry.get())
    print('Sign Up...')
    account=accountentry.get()
    password=passwordentry.get()
    try:
        user=auth.create_user_with_email_and_password(account,password)
        print('Successfully Signup!')
        resultlabel.config(text='Successfully Signup')
    except Exception as e:
        print(f'Create Account Failed...')
        resultlabel['text']='Create Account Failed...'
root.mainloop()


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate()'''

class Car:
    def __init__(self, color):
        self.color=color
        self.next = None
# Initiate the first element of single linked list.


head = Car('RED')
head.next = None




def traverse(head):
    ptr = head
    while ptr!= None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next




traverse(head)
print('Finish traverse!')