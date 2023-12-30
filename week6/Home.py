from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import smtplib
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkscrolledframe import ScrolledFrame
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import Text
import random





def cardcode():
    messagebox.showinfo('cleared','cart cleared!!')
    numl1['text']='0'
    numl2['text']='0'
    numl3['text']='0'
    numl4['text']='0'
    numl5['text']='0'
    numl6['text']='0'
    totalval.set('共消費:0元') 
def add(numlabel,pricelabel):
    numlabel['text']=int(numlabel['text'])+1
    price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
    total=int(totalval.get().split(':')[1].replace('元','').strip())
    totalval.set('共消費:'+str(total+price)+'元')
def minus(numlabel,pricelabel):
    if int(numlabel['text'])>0:
        numlabel['text']=int(numlabel['text'])-1
        price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
        total=int(totalval.get().split(':')[1].replace('元','').strip())
        totalval.set('共消費:'+str(total-price)+'元')
    else:
        messagebox.showwarning('showwarning','The number of product can\'t be below 0')
def sell():
    ana=messagebox.askyesno('Pay','are you sure to pay up')
    print(ana)
    if ana==True:
        payup=Toplevel()
        payup.geometry('850x850')
        card=Label(payup, text='please enter your card code.')
        card.grid(row=0,column=0)
        cardenter=ttk.Entry(payup)
        cardenter.grid(row=0,column=4)
        cardenterbutton=Button(payup,text='enter',command=cardcode)
        cardenterbutton.grid(row=1,column=4)
        payup.mainloop()
def showdetail():
    detailWindow =Toplevel(home)
    detailWindow.geometry('850x250')
    table=ttk.Treeview(detailWindow,columns=['Unit Price','Quantity','SUbtotal'])
    table.heading('#0',text='Product Name')
    table.heading('#1',text='Unit Price')
    table.heading('#2',text='Quanity')
    table.heading('#3',text='Subtotal')
    table.column('#0', width=250,anchor=CENTER)
    table.column('#1',anchor=CENTER)
    table.column('#2',anchor=CENTER)
    table.column('#3', anchor=CENTER)
    table.tag_configure('totalcolor',background='#E7E2E2')
#hamburger
# banna
# cheery
# rawSalmon
# pear
# mango
# soup
# strawberry
# panCakes
# pineapple
# lemon
# apple
# beef
# beefNoodles
# error1
# error2
# error4
# error3
    s1=int(numl1['text'])*int(hamburgerPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=hamburgert1['text'],values=[hamburgerPrice['text'],hamburgert1['text'],s1])
    s2=int(numl2['text'])*int(bannaPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=bannat2['text'],values=[bannaPrice['text'],bannat2['text'],s2])
    s3=int(numl3['text'])*int(cheeryPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=cheeryt3['text'],values=[cheeryPrice['text'],cheeryt3['text'],s3])
    s4=int(numl4['text'])*int(rawSalmonPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=rawSalmont4['text'],values=[rawSalmonPrice['text'],rawSalmont4['text'],s4])
    s5=int(numl5['text'])*int(pearsPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=pearst5['text'],values=[pearsPrice['text'],pearst5['text'],s5])
    s6=int(numl6['text'])*int(mangoPrice['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=mangot6['text'],values=[mangoPrice['text'],mangot6['text'],s6])
    # s7=int(numl7['text'])*int(pl7['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel7['text'],values=[pl7['text'],namel7['text'],s7])
    # s8=int(numl8['text'])*int(pl8['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel8['text'],values=[pl8['text'],namel8['text'],s8])
    # s9=int(numl9['text'])*int(pl9['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel9['text'],values=[pl9['text'],namel9['text'],s9])
    # s10=int(numl10['text'])*int(pl10['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel10['text'],values=[pl10['text'],namel10['text'],s10])
    # s11=int(numl11['text'])*int(pl11['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel11['text'],values=[pl11['text'],namel11['text'],s11])
    # s12=int(numl12['text'])*int(pl12['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel12['text'],values=[pl12['text'],namel12['text'],s12])
    # s13=int(numl13['text'])*int(pl13['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel13['text'],values=[pl13['text'],namel13['text'],s13])
    # s14=int(numl14['text'])*int(pl14['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel14['text'],values=[pl14['text'],namel14['text'],s14])
    # s15=int(numl15['text'])*int(pl15['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel15['text'],values=[pl15['text'],namel15['text'],s15])
    # s16=int(numl16['text'])*int(pl16['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel16['text'],values=[pl16['text'],namel16['text'],s16])
    # s17=int(numl17['text'])*int(pl17['text'].split('.')[1].replace(',','').strip())
    # table.insert('',index='end',text=namel17['text'],values=[pl17['text'],namel17['text'],s17])
    total=s1+s2+s3+s4+s5+s6
    table.insert('',index='end',text='Total',values=['','',total],tag=('totalcolor'))
    table.grid(row=0,column=0)
    detailWindow.mainloop()


import pyrebase
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
logwin=Tk()

loginlabel=Label(logwin,text='Login page')
accountlabel=Label(logwin,text='Account')
passwordlabel=Label(logwin,text='Password')
resultlabel=Label(logwin,text='')

accountentry=Entry(logwin)
passwordentry=Entry(logwin, show='*')
signupbutton=Button(logwin,text='Sign up', width=10,command=lambda:addUser(logwin, accountentry, passwordentry))

loginlabel.pack(pady=5)
accountlabel.pack(pady=5)
passwordlabel.pack(pady=5)
resultlabel.pack(pady=5)
accountentry.pack(pady=5)
signupbutton.pack(pady=5)
passwordentry.pack(pady=5)
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
logwin.mainloop()



def closerank(event):
    rankyesno=messagebox.askyesno('destroy','are you sure to destroy window rank?')
    if rankyesno==True:
        rank.destroy()
def RankWin():
    rank=Toplevel(home)
    rank.geometry('1920x1200')
    homeB=Image.open("project/Screenshot 2023-03-26 212121.png")
    homeB=homeB.resize((80,80))
    global tk_img2
    tk_img2=ImageTk.PhotoImage(homeB)
    homeLb=Button(rank,image=tk_img2,width=80,height=80,command=rank.destroy)
    homeLb.grid(row=0,column=0,sticky=W+E)
    table1=ttk.Treeview(rank,columns=['Unit Price','Rank', 'Ratings'])
    table1.heading('#0',text='Product Name')
    table1.heading('#1',text='Unit Price')
    table1.heading('#2',text='Rank')
    table1.heading('#3',text='Ratings')
    table1.column('#0', width=250,anchor=CENTER)
    table1.column('#1',anchor=CENTER)
    table1.column('#2',anchor=CENTER)
    table1.column('#3', anchor=CENTER)
    table1.tag_configure('totalcolor',background='#E7E2E2')
    table1.insert('',index='end',text=hamburgert1['text'],values=[hamburgerPrice['text'],'No.2',4.5])
    table1.insert('',index='end',text=bannat2['text'],values=[bannaPrice['text'],'No.7',2.9])
    table1.insert('',index='end',text=cheeryt3['text'],values=[cheeryPrice['text'],'No.5',3.2])
    table1.insert('',index='end',text=rawSalmont4['text'],values=[rawSalmonPrice['text'],'No.3',4.3])
    table1.insert('',index='end',text=pearst5['text'],values=[pearsPrice['text'],'No.6',3.0])
    table1.insert('',index='end',text=mangot6['text'],values=[mangoPrice['text'],'No.4',4.0])
    table1.grid(row=1,column=0,columnspan=10,sticky=W)
    rank.bind('<Control- w>',closerank)
    rank.mainloop()
    

def showstockdetail():
    showstockdetailwin=Toplevel(home)
    stockname=Label(showstockdetailwin,text='Beef Noodle',font=('Inter',30))
    stockname.grid(row=0,column=1,sticky=W)
    salestate=Label(showstockdetailwin,text='Discounts:  ',font=20)
    salestate.grid(row=1,column=0)
    sale=Image.open("python_2023Autumn/2023AutumnProject/30%off_sale.jpg")
    sale=sale.resize((80,80))
    global tk_img0
    tk_img0=ImageTk.PhotoImage(sale)
    saleLb=Label(showstockdetailwin,image=tk_img0,width=80,height=80)
    saleLb.grid(row=2,column=0,sticky=W+E)
    rating=Label(showstockdetailwin,text='Rates:',font=20)
    rating.grid(row=3,column=0)
    showrate=Label(showstockdetailwin,text='unknown user\nThe beef was very soft and easy to eat, and it was rich in taste. I had better tasting beef in a beef noodle soup but this is definitely in the top 3. \nThe soup was also very good. There is also a free option of adding a yellow-orange colored "seasoning". At first I did not know what it was, \nbut after putting some on my soup and mixing it, there were red circles forming on top of my soup, meaning there was oil. Also, after adding it, the soup became spicier.\n unkown user\n The stock is indeed very rich, and flavors. When add the lard both spicy or not-so-spicy, it brings out the richness of the taste. \nI did not add other condiments readily on the table. The serving of the beef is reasonable and tender. The noodle though is not as chewy as YK.',font=('Inter',15 ))
    showrate.grid(row=4,column=0,sticky=W)
    avergerate=Label(showstockdetailwin,text='Average ratings',font=20)
    avergerate.grid(row=5,column=0)
    ratestar=Image.open("python_2023Autumn/2023AutumnProject/star_rating.png")
    ratestar=ratestar.resize((360,360))
    global tk_img1
    tk_img1=ImageTk.PhotoImage(ratestar)
    ratestar=Label(showstockdetailwin,image=tk_img1,width=300,height=240)
    ratestar.grid(row=6,column=0,sticky=W+E)
def closetab(event):
    homeyesno=messagebox.askyesno('destroy','are you sure to destroy window home?')
    if homeyesno==True:
        home.destroy()









home=Tk()
home.title('KubeTech Shop')
home.geometry('1920x1080')

# Create a ScrolledFrame widget
sframe1 = ScrolledFrame(home,width=1920, height=2000,bg='#F0F0F0')
sframe1.grid(row=11,column=19)
sframe1.bind_arrow_keys(home)
sframe1.bind_scroll_wheel(home)
inner_frame = sframe1.display_widget(Frame)

home.bind('<Control- w>',closetab)

    

ShoppingCart=Image.open("python_2023Autumn/2023AutumnProject/LOGO.png")
ShoppingCart=ShoppingCart.resize((80,80))
ShoppingCart=ImageTk.PhotoImage(ShoppingCart)



titlelabel=Label(inner_frame,image=ShoppingCart,width=80,height=40)
titlelabel.grid(row=0,column=0,sticky=W)
rank=Button(inner_frame,text='rank',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=RankWin)
rank.grid(row=0,column=1,sticky=W+E)
loginbutton=Button(inner_frame,text='會員登入/註冊',font=('Inter',18),fg='#1E1E1E',bg='#F8DCDC',width=10,pady=2,command=logWin)
loginbutton.grid(row=0,column=3,sticky=E,padx=5)




banner=Image.open("python_2023Autumn/2023AutumnProject/beef_noodle.jpg")
banner=banner.resize((750,500))
banner=ImageTk.PhotoImage(banner)
bannerLabel=Button(inner_frame,image=banner,width=750,height=500,command=showstockdetail)
bannerLabel.grid(row=1,column=0,columnspan=10,padx=5)




stockHamburgers=Image.open("python_2023Autumn/2023AutumnProject/hamburger.jpg")
stockHamburgers=stockHamburgers.resize((300,225))
stockHamburgers=ImageTk.PhotoImage(stockHamburgers)
HamburgersLabel=Label(inner_frame,image=stockHamburgers,width=280,height=225)
HamburgersLabel.grid(row=2,column=0,columnspan=2,sticky=W,padx=5)
stockBanna=Image.open("python_2023Autumn/2023AutumnProject/Bananas-5c6a36a346e0fb0001f0e4a3.jpg")
stockBanna=stockBanna.resize((300,200))
stockBanna=ImageTk.PhotoImage(stockBanna)
BannaLabel=Label(inner_frame,image=stockBanna,width=270,height=200)
BannaLabel.grid(row=2,column=2,columnspan=2,sticky=W,padx=5)
stockCherries=Image.open("python_2023Autumn/2023AutumnProject/cherries.jpg")
stockCherries=stockCherries.resize((300,298))
stockCherries=ImageTk.PhotoImage(stockCherries)
CherriesLabel=Label(inner_frame,image=stockCherries,width=250,height=250)
CherriesLabel.grid(row=2,column=4,columnspan=2,sticky=W,padx=5)
stockSalmon=Image.open("python_2023Autumn/2023AutumnProject/raw_salmon.jpg")
stockSalmon=stockSalmon.resize((300,150))
stockSalmon=ImageTk.PhotoImage(stockSalmon)
SalmonLabel=Label(inner_frame,image=stockSalmon,width=280,height=150)
SalmonLabel.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
stockPears=Image.open("python_2023Autumn/2023AutumnProject/pear.jpg")
stockPears=stockPears.resize((300,150))
stockPears=ImageTk.PhotoImage(stockPears)
PearsLabel=Label(inner_frame,image=stockPears,width=260,height=150)
PearsLabel.grid(row=2,column=8,columnspan=2,sticky=W,padx=5)
stockMango=Image.open("python_2023Autumn/2023AutumnProject/mango.jpg")
stockMango=stockMango.resize((300,300))
stockMango=ImageTk.PhotoImage(stockMango)
MangoLabel=Label(inner_frame,image=stockMango,width=300,height=300)
MangoLabel.grid(row=5,column=0,columnspan=2,sticky=W,padx=5)
# stockSoup=Image.open("project/minestrone-soup-recipe-22.jpg")
# stockSoup=stockSoup.resize((202,200))
# stockSoup=ImageTk.PhotoImage(stockSoup)
# SoupLabel=Label(inner_frame,image=stockSoup,width=220,height=200)
# SoupLabel.grid(row=2,column=10,columnspan=2,sticky=W,padx=5)
# stockStrawberry=Image.open("project/p0dx4wkz.jpg")
# stockStrawberry=stockStrawberry.resize((202,200))
# stockStrawberry=ImageTk.PhotoImage(stockStrawberry)
# StrawberryLabel=Label(inner_frame,image=stockStrawberry,width=202,height=200)
# StrawberryLabel.grid(row=2,column=14,columnspan=2,sticky=W,padx=5)
# stockPancakes=Image.open("project/pexels-ash-376464.jpg")
# stockPancakes=stockPancakes.resize((202,200))
# stockPancakes=ImageTk.PhotoImage(stockPancakes)
# PancakesLabel=Label(inner_frame,image=stockPancakes,width=202,height=200)
# PancakesLabel.grid(row=2,column=16,columnspan=2,sticky=W,padx=5)
# stockPineapple=Image.open("project/photo-1550258987-190a2d41a8ba.jpg")
# stockPineapple=stockPineapple.resize((202,200))
# stockPineapple=ImageTk.PhotoImage(stockPineapple)
# PineappleLabel=Label(inner_frame,image=stockPineapple,width=202,height=200)
# PineappleLabel.grid(row=6,column=0,columnspan=2,sticky=W,padx=5)
# stockLemon=Image.open("project/raw-green-organic-golden-pomelo-1078669424.jpg")
# stockLemon=stockLemon.resize((202,200))
# stockLemon=ImageTk.PhotoImage(stockLemon)
# LemonLabel=Label(inner_frame,image=stockLemon,width=202,height=200)
# LemonLabel.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stockApple=Image.open("project/shutterstock_226100671.jpg")
# stockApple=stockApple.resize((202,200))
# stockApple=ImageTk.PhotoImage(stockApple)
# AppleLabel=Label(inner_frame,image=stockApple,width=202,height=200)
# AppleLabel.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stockSteak=Image.open("project/sous-vide-brisket-mfs-193-4x3-1-24930daf16854a9091eaff1503aac157.jpg")
# stockSteak=stockSteak.resize((202,200))
# stockSteak=ImageTk.PhotoImage(stockSteak)
# SteakLabel=Label(inner_frame,image=stockSteak,width=202,height=200)
# SteakLabel.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stockBeefNoddle=Image.open("project/taiwanese-beef-noodle-soup-4777014-hero-01-e06a464badec476684e513cad44612da.jpg")
# stockBeefNoddle=stockBeefNoddle.resize((202,200))
# stockBeefNoddle=ImageTk.PhotoImage(stockBeefNoddle)
# BeefNoddleLabel=Label(inner_frame,image=stockBeefNoddle,width=202,height=200)
# BeefNoddleLabel.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stock4041=Image.open("project/istockphoto-654971856-612x612.jpg")
# stock4041=stock4041.resize((202,200))
# stock4041=ImageTk.PhotoImage(stock4041)
# error1Label=Label(inner_frame,image=stock4041,width=202,height=200)
# error1Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stock4042=Image.open("project/istockphoto-654971856-612x612.jpg")
# stock4042=stock4042.resize((202,200))
# stock4042=ImageTk.PhotoImage(stock4042)
# error2Label=Label(inner_frame,image=stock4042,width=202,height=200)
# error2Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# stock4043=Image.open("project/istockphoto-654971856-612x612.jpg")
# stock4043=stock4043.resize((202,200))
# stock4043=ImageTk.PhotoImage(stock4043)
# error3Label=Label(inner_frame,image=stock4043,width=202,height=200)
# error3Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)
# hamburger
# banna
# cheery
# rawSalmon
# pear
# mango
# soup
# strawberry
# panCakes
# pineapple
# lemon
# apple
# beef
# beefNoodles
# error1
# error2
# error4
# error3
hamburgert1=Label(inner_frame,text='Hamburger',font=('Inter',15,'bold'),fg='#000000')
hamburgert1.grid(row=3,column=0,columnspan=2,sticky=W,padx=5)
bannat2=Label(inner_frame,text='Banna',font=('Inter',15,'bold'),fg='#000000')
bannat2.grid(row=3,column=2,columnspan=2,sticky=W,padx=5)
cheeryt3=Label(inner_frame,text='Cheery',font=('Inter',15,'bold'),fg='#000000')
cheeryt3.grid(row=3,column=4,columnspan=2,sticky=W,padx=5)
rawSalmont4=Label(inner_frame,text='Raw salmon',font=('Inter',15,'bold'),fg='#000000')
rawSalmont4.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)
pearst5=Label(inner_frame,text='Pears',font=('Inter',15,'bold'),fg='#000000')
pearst5.grid(row=3,column=8,columnspan=2,sticky=W,padx=5)
mangot6=Label(inner_frame,text='Mango',font=('Inter',15,'bold'),fg='#000000')
mangot6.grid(row=6,column=0,columnspan=2,sticky=W,padx=5)
# soupt7=Label(inner_frame,text='soup',font=('Inter',10),fg='#000000')
# soupt7.grid(row=3,column=10,columnspan=2,sticky=W,padx=5)
# strawberryt8=Label(inner_frame,text='strawberry',font=('Inter',10),fg='#000000')
# strawberryt8.grid(row=3,column=14,columnspan=2,sticky=W,padx=5)
# panCakest9=Label(inner_frame,text='pan cakes',font=('Inter',10),fg='#000000')
# panCakest9.grid(row=3,column=16,columnspan=2,sticky=W,padx=5)
# pineapplet10=Label(inner_frame,text='pineapple',font=('Inter',10),fg='#000000')
# pineapplet10.grid(row=3,column=18,columnspan=2,sticky=W,padx=5)
# lemont11=Label(inner_frame,text='lemon',font=('Inter',10),fg='#000000')
# lemont11.grid(row=6,column=0,columnspan=2,sticky=W,padx=5)
# applet12=Label(inner_frame,text='apple',font=('Inter',10),fg='#000000')
# applet12.grid(row=6,column=2,columnspan=2,sticky=W,padx=5)
# beeft13=Label(inner_frame,text='beef',font=('Inter',10),fg='#000000')
# beeft13.grid(row=6,column=4,columnspan=2,sticky=W,padx=5)
# beefNoodlest14=Label(inner_frame,text='beef noodles',font=('Inter',10),fg='#000000')
# beefNoodlest14.grid(row=6,column=6,columnspan=2,sticky=W,padx=5)
# errort15=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# errort15.grid(row=6,column=8,columnspan=2,sticky=W,padx=5)
# errort16=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# errort16.grid(row=6,column=10,columnspan=2,sticky=W,padx=5)
# errort17=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# errort17.grid(row=6,column=10,columnspan=2,sticky=W,padx=5)

#
hamburgerPrice=Label(inner_frame,text='NT.89',font=('Inter',15),fg='#000000')
hamburgerPrice.grid(row=4,column=0,sticky=W,padx=5)

bannaPrice=Label(inner_frame,text='NT.40',font=('Inter',15),fg='#000000')
bannaPrice.grid(row=4,column=2,sticky=W,padx=5)

cheeryPrice=Label(inner_frame,text='NT.55',font=('Inter',15),fg='#000000')
cheeryPrice.grid(row=4,column=4,sticky=W,padx=5)

rawSalmonPrice=Label(inner_frame,text='NT.65',font=('Inter',15),fg='#000000')
rawSalmonPrice.grid(row=4,column=6,sticky=W,padx=5)

pearsPrice=Label(inner_frame,text='NT.60',font=('Inter',15),fg='#000000')
pearsPrice.grid(row=4,column=8,sticky=W,padx=5)

mangoPrice=Label(inner_frame,text='NT.20',font=('Inter',15),fg='#000000')
mangoPrice.grid(row=7,column=0,sticky=W,padx=5)    

# soupPrice=Label(inner_frame,text='NT.50',font=('Inter',10),fg='#000000')
# soupPrice.grid(row=4,column=10,sticky=W,padx=5)

# strawberryPrice=Label(inner_frame,text='NT.120',font=('Inter',10),fg='#000000')
# strawberryPrice.grid(row=4,column=14,sticky=W,padx=5)

# panCakestPrice=Label(inner_frame,text='NT.110',font=('Inter',10),fg='#000000')
# panCakestPrice.grid(row=4,column=16,sticky=W,padx=5)

# pineapplePrice=Label(inner_frame,text='NT.115',font=('Inter',10),fg='#000000')
# pineapplePrice.grid(row=4,column=18,sticky=W,padx=5)

# lemonPrice=Label(inner_frame,text='NT.60',font=('Inter',10),fg='#000000')
# lemonPrice.grid(row=4,column=6,sticky=W,padx=5)

# applePrice=Label(inner_frame,text='NT.25',font=('Inter',10),fg='#000000')
# applePrice.grid(row=4,column=6,sticky=W,padx=5)

# beefPrice=Label(inner_frame,text='NT.30',font=('Inter',10),fg='#000000')
# beefPrice.grid(row=4,column=6,sticky=W,padx=5)

# beefNoodlesPrice=Label(inner_frame,text='NT.499',font=('Inter',10),fg='#000000')
# beefNoodlesPrice.grid(row=4,column=6,sticky=W,padx=5)

# error1Price=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# error1Price.grid(row=4,column=6,sticky=W,padx=5)

# error2Price=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# error2Price.grid(row=4,column=6,sticky=W,padx=5)

# error3Price=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# error3Price.grid(row=4,column=6,sticky=W,padx=5)

# error4Price=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
# error4Price.grid(row=4,column=6,sticky=W,padx=5)


# hamburger
# banna
# cheery
# rawSalmon
# pear
# mango
# soup
# strawberry
# panCakes
# pineapple
# lemon
# apple
# beef
# beefNoodles
# error1
# error2
# error4
# error3
mb1=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl1,hamburgerPrice))
mb1.grid(row=4,column=1,sticky=W)
numl1=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl1.grid(row=4,column=1)
ab1=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl1,hamburgerPrice))
ab1.grid(row=4,column=1,sticky=E)

mb2=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl2,bannaPrice))
mb2.grid(row=4,column=3,sticky=W)
numl2=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl2.grid(row=4,column=3)
ab2=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl2,bannaPrice))
ab2.grid(row=4,column=3,sticky=E)

mb3=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl3,cheeryPrice))
mb3.grid(row=4,column=5,sticky=W)
numl3=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl3.grid(row=4,column=5)
ab3=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl3,cheeryPrice))
ab3.grid(row=4,column=5,sticky=E)

mb4=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl4,rawSalmonPrice))
mb4.grid(row=4,column=7,sticky=W)
numl4=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl4.grid(row=4,column=7)
ab4=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl4,rawSalmonPrice))
ab4.grid(row=4,column=7,sticky=E)

mb5=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl5,pearsPrice))
mb5.grid(row=4,column=9,sticky=W)
numl5=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl5.grid(row=4,column=9)
ab5=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl5,pearsPrice))
ab5.grid(row=4,column=9,sticky=E)

mb6=Button(inner_frame,text='-',width=1,font=('Inter',15),command=lambda: minus(numl6,mangoPrice))
mb6.grid(row=7,column=1,sticky=W)
numl6=Label(inner_frame,text='0',width=3,font=('Inter',15,'bold'),fg='#000000')
numl6.grid(row=7,column=1)
ab6=Button(inner_frame,text='+',width=1,font=('Inter',15),command=lambda: add(numl6,mangoPrice))
ab6.grid(row=7,column=1,sticky=E)

# mb7=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl7,pl4))
# mb7.grid(row=4,column=13,sticky=W)
# numl7=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl7.grid(row=4,column=13)
# ab7=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl7,pl4))
# ab7.grid(row=4,column=13,sticky=E)

# mb8=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl8,pl4))
# mb8.grid(row=4,column=15,sticky=W)
# numl8=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl8.grid(row=4,column=15)
# ab8=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl8,pl4))
# ab8.grid(row=4,column=15,sticky=E)

# mb9=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl9,pl4))
# mb9.grid(row=4,column=17,sticky=W)
# numl9=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl9.grid(row=4,column=17)
# ab9=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl9,pl4))
# ab9.grid(row=4,column=17,sticky=E)

# mb10=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl10,pl4))
# mb10.grid(row=4,column=7,sticky=W)
# numl10=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl10.grid(row=4,column=7)
# ab10=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl10,pl4))
# ab10.grid(row=4,column=7,sticky=E)

# mb11=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl11,pl4))
# mb11.grid(row=4,column=7,sticky=W)
# numl11=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl11.grid(row=4,column=7)
# ab11=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl11,pl4))
# ab11.grid(row=4,column=7,sticky=E)

# mb12=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl12,pl4))
# mb12.grid(row=4,column=7,sticky=W)
# numl12=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl12.grid(row=4,column=7)
# ab12=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl12,pl4))
# ab12.grid(row=4,column=7,sticky=E)

# mb13=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl13,pl4))
# mb13.grid(row=4,column=7,sticky=W)
# numl13=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl13.grid(row=4,column=7)
# ab13=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl13,pl4))
# ab13.grid(row=4,column=7,sticky=E)

# mb14=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl14,pl4))
# mb14.grid(row=4,column=7,sticky=W)
# numl14=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl14.grid(row=4,column=7)
# ab14=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl14,pl4))
# ab14.grid(row=4,column=7,sticky=E)

# mb15=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl15,pl4))
# mb15.grid(row=4,column=7,sticky=W)
# numl15=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl5.grid(row=4,column=7)
# ab15=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl15,pl4))
# ab15.grid(row=4,column=7,sticky=E)

# mb16=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl4,pl4))
# mb16.grid(row=4,column=7,sticky=W)
# numl16=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl16.grid(row=4,column=7)
# ab16=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl4,pl4))
# ab16.grid(row=4,column=7,sticky=E)

# mb17=Button(inner_frame,text='-',font=('Inter',10),command=lambda: minus(numl4,pl4))
# mb17.grid(row=4,column=7,sticky=W)
# numl17=Label(inner_frame,text='0',font=('Inter',10,'bold'),fg='#000000')
# numl17.grid(row=4,column=7)
# ab17=Button(inner_frame,text='+',font=('Inter',10),command=lambda: add(numl4,pl4))
# ab17.grid(row=4,column=7,sticky=E)







detaillistbutton=Button(inner_frame,text='詳細清單',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=showdetail)


cartimg=Image.open('python_2023Autumn/2023AutumnProject/LOGO.png')
cartimg=cartimg.resize((30,30))
cartimg=ImageTk.PhotoImage(cartimg)
shoppingcartlabel=Label(inner_frame,image=cartimg,width=30,height=30)

totalval=StringVar()
totalval.set('共消費:0元') 
totallabel=Label(inner_frame,textvariable=totalval,font=('Inter',10),fg='#000000')
checkoutbutton=Button(inner_frame,text='結帳',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=sell)

home.rowconfigure(5,weight=2)
shoppingcartlabel.grid(row=11,column=5,sticky=E+S)
totallabel.grid(row=11,column=5,columnspan=2,sticky=W+S)
checkoutbutton.grid(row=11,column=10,sticky=E+S)
detaillistbutton.grid(row=11,column=0,sticky=S+W,padx=5,pady=1)

home.mainloop()