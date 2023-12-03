'''import pyrebase
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

def signup():
    email=input('Please enter your email')
    password=input('Please enter your password')
    try:
        user=auth.create_user_with_email_and_password(email,password)
        print('Successfully sign up')
    except:
        print('Email account already exist')
#signup()

def login():
    print('Log in...')
    email=input('Please enter your email')
    password=input('Please enter your password')

    try:

        user = auth.sign_in_with_email_and_password(email, password)
        print ("Successfully logged in!")
        print (user)
        
    except:
        print('Invalid email or password')
login()'''


'''class Car:
    def __init__(self, color):
        self.color=color
        self.next = None
# Initiate the first element of single linked list.
head = Car('red')
head.next = None'''

'''class Car:
    def __init__(self, color):
        self.color=color
        self.next = None
head = Car('red')
head.next = None
def traverse(head):
    ptr = head
    while ptr!= None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next

'''
