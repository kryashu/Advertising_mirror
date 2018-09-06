from Tkinter import *
import requests
import json
import platform
import uuid
import os
import time
import tkMessageBox
def getserial():
   try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
   except:
    cpuserial = "ERROR000000000" 
   return cpuserial
cpuserial = getserial()
def work(*args):
    g=variable.get()    
    if g=='Select':
        d=""    
    else:
        URL1 = "http://smartadvertisement.rannlabprojects.com/BusinessNameMacAddress"
        print MacId
        data = {'MacAddress':MacId,'BusinessName':g}
        r = requests.post(url = URL1, data = data)
        data1=r.json()
        obj1=json.loads(data1)
        if obj1=='0': 
            master.destroy()   
        if obj1=='1':
               master.destroy()
        pastebin_url = r.text
          
URL = "http://smartadvertisement.rannlabprojects.com/businessName"
PARAMS = {}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
obj = json.loads(data)
obj_size = len(obj)
master = Tk()
master.title('Welcome to Registration Page')
master.overrideredirect(True)
#master.configure(background="#87ceeb")
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
var = StringVar()
var.set("Select Your Bussiness Name: ")
w1= Label(master, textvariable=var,font = "Arial 15 bold")
w2= Label(master, text="Welcome to Device Registration",font = "Arial 20 bold",bg="#87ceeb",fg="White")
w2.pack(fill="x")
"""
canvas = Canvas(master)      
canvas.place(x=400,y=350)      
img = PhotoImage(file="download.png")      
canvas.create_image(20,20, anchor=NW, image=img)"""
variable = StringVar(master)
variable.set("Select Name")
newlist = []
for i in range(0,obj_size):
    d1=obj[i]['CompanyName']
    newlist.append(d1)
w1.place(x=350,y=100)
w = OptionMenu(master, variable,*newlist)
w.config(font=('calibri',(10)),width=20)
w['menu'].config(font=('calibri ',(10)),bg='white')
w.place(x=680,y=100)
MacId =':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
var = StringVar()
var.set("MAC ID : "+MacId)
ww= Label(master, textvariable=var,font = "Arial 15 bold") 
ww.place(x=420,y=200)
var = StringVar()
var.set("CpuSerial: "+cpuserial)
label3= Label(master, textvariable=var,font = "Arial 15 bold")
label3.place(x=400,y=160)
button = Button(master, text="Register",font="Arial 15 bold", fg="red",command=work)
button.place(x=470,y=300)
MacId =':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
URL = "http://smartadvertisement.rannlabprojects.com/IsRegistered"
PARAMS ={"Mac":MacId}
r = requests.post(url = URL , data = PARAMS)
data = r.json()
dat = json.loads(data)
flag = dat[0]['IsPresent']
if flag == 1:
  Button(master, text="Exit",font="Arial 15 bold",fg="Black",command=master.destroy).place(x=600,y=300)
master.mainloop()
