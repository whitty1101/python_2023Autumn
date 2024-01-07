
# 引入 tkinter module
from tkinter import *
import tkinter.ttk as ttk
# 引入 Pillow module
from PIL import Image, ImageTk
# 引入 tkinter 的 messagebox
from tkinter import messagebox
import pyrebase
import os

config= {
  "apiKey": "AIzaSyCyAHFBC50HzoqBMSzCPKxSYt_whaqUy8w",
  "authDomain": "fir-test-5e7d6.firebaseapp.com",
  "projectId": "fir-test-5e7d6",
  "storageBucket": "fir-test-5e7d6.appspot.com",
  "messagingSenderId": "717063514473",
  "appId": "1:717063514473:web:e3e1046f010ac91d2b75f8",
  "databaseURL":"",
  "serviceAccount":"../../fir-test-5e7d6-firebase-adminsdk-opd28-ef72fd484e.json"
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
        file.download_to_filename(file.name)

# 建立主視窗 Frame
root = Tk()
# 設定視窗標題
root.title('KubeTech Shop')
# 設定視窗大小
root.geometry('880x650')

# click the button to add 1 to the number
def add(numlabel, pricelabel):
    # numlabel的text +1
    numlabel['text'] = int(numlabel['text'])+1
    price = int(pricelabel['text'].split('.')[1].replace(',','').strip())
    total = int(totalval.get().split(':')[1].replace('元','').strip())
    totalval.set('共消費: '+str(total+price)+' 元')

# click the button to minus 1 to the number
def minus(numlabel, pricelabel):
    # 當numlabel大於0時，才會進行減1
    if int(numlabel['text'])>0:
        # numlabel的text -1
        numlabel['text'] = int(numlabel['text'])-1
        price = int(pricelabel['text'].split('.')[1].replace(',','').strip())
        total = int(totalval.get().split(':')[1].replace('元','').strip())
        totalval.set('共消費: '+str(total-price)+' 元')
    # 當numlabel小於0時，跳出警告訊息框
    else:
        messagebox.showwarning('showwarning', 'The number of products can\'t be below 0.')

# verify user's account and password
def verifyUser(view, accountentry, passwordentry):
    if accountentry.get()=='Prince' and passwordentry.get()=='kubetech':
        # if account and password are correct then close the login windows
        view.destroy()
        loginbutton.destroy()
        afterloginlabel = Label(root, text='Prince',  font=('Inter', 18)).grid(row=0, column=7, sticky=E, padx=5)
    else:
        messagebox.showwarning('showwarning', 'Please input correct account and password!')

# click button to login
def login():
    # create login Windows
        loginWindow = Toplevel(root)
        loginWindow.geometry('280x200')
        # create Label in login Windows
        loginlabel = Label(loginWindow, text = 'User Login')
        accountlabel = Label(loginWindow, text = 'Account')
        passwordlabel = Label(loginWindow, text = 'Password')

        # create entry box in login windows
        accountentry = Entry(loginWindow)
        passwordentry = Entry(loginWindow, show='*')

        # create Button in login Windows
        loginbutton = Button(loginWindow, text = 'Login', width=10, command=lambda: verifyUser(loginWindow, accountentry, passwordentry))

        # set layout
        loginlabel.grid(row=0, column=0 ,columnspan=2, pady=5)
        accountlabel.grid(row=1, column=0, sticky=W, padx=5)
        accountentry.grid(row=1, column=1, sticky=W+E+N+S)
        passwordlabel.grid(row=2, column=0, sticky=W, padx=5)
        passwordentry.grid(row=2, column=1, sticky=W+E+N+S)
        loginbutton.grid(row=3, column=0, columnspan=2, pady=10)

        # 執行新視窗程式
        loginWindow.mainloop()

# show shopping cart detail
def showdetail():

    detailWindow = Toplevel(root)
    detailWindow.geometry('850x250')

    table = ttk.Treeview(detailWindow, columns=['Product Name', 'Unit Price', 'Quantity'])
    # create columns title
    table.heading('#0', text='Product Name')
    table.heading('#1', text='Unit Price')
    table.heading('#2', text='Quantity')
    table.heading('#3', text='Subtotal')
    # set column type 
    table.column('#0', width=250, anchor=CENTER)
    table.column('#1', anchor=CENTER)
    table.column('#2', anchor=CENTER)
    table.column('#3', anchor=CENTER)
    # 建立内容,從total行是用淺藍色底
    table.tag_configure('totalcolor', background='#E7E2E2')

    # input column content
    subtotal1 = int(p1numlabel['text']) * int(p1pricelabel['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=p1namelabel['text'],values=(p1pricelabel['text'],p1numlabel['text'], subtotal1))
    subtotal2 = int(p2numlabel['text']) * int(p2pricelabel['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=p2namelabel['text'],values=(p2pricelabel['text'],p2numlabel['text'], subtotal2))
    subtotal3 = int(p3numlabel['text']) * int(p3pricelabel['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=p3namelabel['text'],values=(p3pricelabel['text'],p3numlabel['text'], subtotal3))
    subtotal4 = int(p4numlabel['text']) * int(p4pricelabel['text'].split('.')[1].replace(',',''))
    table.insert('',index='end',text=p4namelabel['text'],values=(p4pricelabel['text'],p4numlabel['text'], subtotal4))
    total = subtotal1+subtotal2+subtotal3+subtotal4
    table.insert('',index='end',text='Total',values=['','', total], tags=('totalcolor'))

    table.pack()

    detailWindow.mainloop()



# upper Label & Button of winodw
titleimg = Image.open('./project_images/logo_tree.png')
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image=titleimg, width=32, height=32)
sofabutton = Button(root, text='沙發', font=('Inter', 18), fg='#1E1E1E', bg='#ECE8E7', width=5, pady=2)
beddingbutton = Button(root, text='寢具', font=('Inter', 18), fg='#1E1E1E', bg='#ECE8E7', width=5, pady=2)
kitchenwarebutton = Button(root, text='廚具', font=('Inter', 18), fg='#1E1E1E', bg='#ECE8E7', width=5, pady=2)
loginbutton = Button(root, text='會員登入/註冊', font=('Inter', 18), fg='#1E1E1E', bg='#F8DCDC', width=12, pady=2, command=login)
bannerimg = Image.open('./project_images/banner.jpg')
bannerimg = bannerimg.resize((852,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image=bannerimg, width=852, height=298)

# upper layout
titlelabel.grid(row=0, column=0, sticky=W)
sofabutton.grid(row=0, column=1, sticky=E+W, padx=5)
beddingbutton.grid(row=0, column=2, sticky=E+W, padx=5)
kitchenwarebutton.grid(row=0, column=3, sticky=E+W, padx=5)
loginbutton.grid(row=0, column=7, sticky=E, padx=5)
bannerlabel.grid(row=1,column=0, columnspan=8, padx=5)


# Product1 Label & Button 元件
p1img = Image.open('./project_images/sofa1.jpg')
p1img = p1img.resize((202,200))
p1img = ImageTk.PhotoImage(p1img)
p1piclabel = Label(root, image=p1img, width=202, height=200)
p1namelabel = Label(root, text='三人座沙發, grann/bomstad 黑色/金屬', font=('Inter', 11), fg='#000000')
p1pricelabel = Label(root, text='NT.28,900', font=('Inter', 10), fg='#000000')
p1numlabel = Label(root, text='0', font=('Inter', 12, 'bold'), fg='#000000')
p1addbutton = Button(root, text='+', font=('Inter', 10), fg='#1E1E1E', bg='#E7E2E2', command=lambda: add(p1numlabel, p1pricelabel))
p1minusbutton = Button(root, text='-', font=('Inter', 10), fg='#1E1E1E', bg='#E7E2E2', command=lambda: minus(p1numlabel, p1pricelabel))

# Product1 Layout
p1piclabel.grid(row=2, column=0, columnspan=2,sticky=W, padx=5)
p1namelabel.grid(row=3, column=0,columnspan=2,sticky=W, padx=5)
p1pricelabel.grid(row=4, column=0, sticky=W, padx=5)
p1minusbutton.grid(row=4, column=1, sticky=W, padx=(15, 0))
p1numlabel.grid(row=4, column=1, sticky=W+E+N+S, padx=(5, 0))
p1addbutton.grid(row=4, column=1, sticky=E, padx=(0, 10))


# Product2 Label & Button 元件
p2img = Image.open('./project_images/sofa2.jpg')
p2img = p2img.resize((202,200))
p2img = ImageTk.PhotoImage(p2img)
p2piclabel = Label(root, image=p2img, width=202, height=200)
p2namelabel = Label(root, text='三人座沙發, grann/bomstad 黑色/木材', font=('Inter', 11), fg='#000000')
p2pricelabel = Label(root, text='NT.28,900', font=('Inter', 10), fg='#000000')
p2numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p2addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: add(p2numlabel, p2pricelabel))
p2minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: minus(p2numlabel, p2pricelabel))

# Product2 Layout
p2piclabel.grid(row=2, column=2, columnspan=2, sticky=W,padx=5)
p2namelabel.grid(row=3, column=2, columnspan=2, sticky=W, padx=5)
p2pricelabel.grid(row=4, column=2, sticky=W, padx=5)
p2minusbutton.grid(row=4, column=3, sticky=W, padx=(25, 0))
p2numlabel.grid(row=4, column=3, sticky=W+E+N+S, padx=(15, 0))
p2addbutton.grid(row=4, column=3, sticky=E, padx=(0, 10))

# Product3 Label & Button 元件
p3img = Image.open('./project_images/sofa3.jpg')
p3img = p3img.resize((202,200))
p3img = ImageTk.PhotoImage(p3img)
p3piclabel = Label(root, image=p3img, width=202, height=200)
p3namelabel = Label(root, text='三人座沙發, grann/bomstad 米色/金屬', font=('Inter', 11), fg='#000000')
p3pricelabel = Label(root, text='NT.28,900', font=('Inter', 10), fg='#000000')
p3numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p3addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: add(p3numlabel, p3pricelabel))
p3minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: minus(p3numlabel, p3pricelabel))

# Product3 Layout
p3piclabel.grid(row=2, column=4, columnspan=2, sticky=W,padx=5)
p3namelabel.grid(row=3, column=4, columnspan=2, sticky=W, padx=5)
p3pricelabel.grid(row=4, column=4, sticky=W, padx=5)
p3minusbutton.grid(row=4, column=5, sticky=W, padx=(10,0))
p3numlabel.grid(row=4, column=5, sticky=W+E+N+S)
p3addbutton.grid(row=4, column=5, sticky=E, padx=(0, 10))

# Product4 Label & Button 元件
p4img = Image.open('./project_images/sofa4.jpg')
p4img = p4img.resize((202,200))
p4img = ImageTk.PhotoImage(p4img)
p4piclabel = Label(root, image=p4img, width=202, height=200)
p4namelabel = Label(root, text='三人座沙發, grann/bomstad 米色/木頭', font=('Inter', 11), fg='#000000')
p4pricelabel = Label(root, text='NT.28,900', font=('Inter', 10), fg='#000000')
p4numlabel = Label(root, text='0', font=('Inter', 14, 'bold'), fg='#000000')
p4addbutton = Button(root, text='+', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: add(p4numlabel, p4pricelabel))
p4minusbutton = Button(root, text='-', font=('Inter', 12), fg='#1E1E1E', bg='#E7E2E2', command=lambda: minus(p4numlabel, p4pricelabel))

# Product4 Layout
p4piclabel.grid(row=2, column=6, columnspan=2, sticky=W,padx=5)
p4namelabel.grid(row=3, column=6, columnspan=2, sticky=W, padx=5)
p4pricelabel.grid(row=4, column=6, sticky=W, padx=5)
p4minusbutton.grid(row=4, column=7, sticky=W, padx=(60,0))
p4numlabel.grid(row=4, column=7, sticky=W+E+N+S, padx=(50, 0))
p4addbutton.grid(row=4, column=7, sticky=E, padx=(0, 10))

# bottom Label & Button of winodw
detaillistbutton = Button(root, text='詳細清單', font=('Inter', 18), fg='#1E1E1E', bg='#ECEDE7', command=showdetail)
cartimg = Image.open('./project_images/Shopping Cart.png')
cartimg = cartimg.resize((30,30))
cartimg = ImageTk.PhotoImage(cartimg)
shppingcartlabel = Label(root, image=cartimg, width=30, height=30)
# 宣告一個文字變數
totalval = StringVar()
totalval.set('共消費: 0 元')
totallabel = Label(root, textvariable=totalval, font=('Inter', 18), fg='#000000')
checkoutbutton = Button(root, text='結帳', font=('Inter', 18), fg='#1E1E1E', bg='#ECEDE7')

# bottom layout
root.rowconfigure(5, weight=2)
detaillistbutton.grid(row=5, column=0, sticky=W+S, padx=5, pady=1)
shppingcartlabel.grid(row=5, column=5,sticky=E+S)
totallabel.grid(row=5, column=6, columnspan=2,sticky=W+S)
checkoutbutton.grid(row=5, column=7, sticky=E+S)


# 執行主程式
root.mainloop()