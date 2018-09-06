from subprocess import *
import threading
import time
import requests
import json
import uuid
import urllib
from threading import Thread
import Adafruit_GPIO
import Adafruit_GPIO.SPI as SPI
import ibmiotf.device
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import pymysql
import os
from datetime import datetime
GPIO.setmode(GPIO.BCM)               #RPi GPIO setup
SPI_PORT   = 0                       #Configuring SPI
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

"""" stri = "https://www.google.co.in"
      data = urllib.urlopen(stri)
except Exception as e:
       print e
       import tkMessageBox
       t = tkMessageBox.showerror("No internet","Connect to network /n Then Click OK")
       if t:
             os.system("sudo init 6")"""
try:
  MacId =':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
  URL = "http://smartadvertisement.rannlabprojects.com/IsRegistered"
  PARAMS ={"Mac":MacId}
  r= requests.post(url = URL , data = PARAMS)
  data = r.json()
  dat = json.loads(data)
  flag = dat[0]['IsPresent']
  if flag == 0:
    os.system("python /home/pi/Rannlab/reg.py")
  else:
    pass
except Exception as e:
    print e
def func2():
    pass
    execfile("/home/pi/Rannlab/Upload_Counts.py")

def func3():
    pass 
    execfile("/home/pi/Rannlab/video.py")
def func4():
    pass
    execfile("/home/pi/Rannlab/Del.py")
def get_video():
    global cnt
    db=pymysql.connect(host="localhost",user="root", passwd="",  db="main")  
    cur = db.cursor()
    sql = "Select id , localcnt from videos order by convert(localcnt,decimal) Asc ;"
    cur.execute(sql)
    for row in cur.fetchall():
            movie = "/home/pi/Videos/"+row[0]+".mp4"
            if os.path.isfile(movie):
                         print "Yes"
                         cnt = str(int(row[1])+1)
                         vid_id = row[0]
                         break
            else:
                movie = "/home/pi/Rannlab/default.mp4"
    db.close()
    return movie,cnt,vid_id
def up_count(i,st,en):
     db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")
     cur = db.cursor()
     sql = "Insert into counts (video,star,end) values (%s,%s,%s);"
     cur.execute(sql,(i,st,en))
     db.commit()
     db.close()

def set_localcnt(cn,n):
    db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")
    cur = db.cursor()
    sql = "Update videos set localcnt = %s where id = %s;"
    cur.execute(sql,(cn,n))
    db.commit()
    db.close()
def main():
   if __name__ == '__main__':
    t1 = Thread(target = func4)
    t2 = Thread(target = func2)
    #t3 =  Thread(target = func1)
    t4 =  Thread(target = func3)
    if t1.isAlive():
       pass
    else:
       t1.start()
       print t1.isAlive()
    if t2.isAlive():
       pass
    else:
       t2.start()
       print t2.isAlive()
    if t4.isAlive():
       pass
    else:
       t4.start()
       print t4.isAlive()
       
if __name__ == '__main__':
    tre = Thread(target=main)
    tre.start()
time.sleep(2)    
while True:
    try:
      os.system('xset dpms force off')
      if (mcp.read_adc(0))>50:
        print "triggered"    
        time.sleep(1)  
        if (mcp.read_adc(0))>50:  
         print mcp.read_adc(0)
         st = str(datetime.now())
         m,cn,vid_id=get_video()
         omxc= Popen(['omxplayer','-b',m])
         print omxc.poll()
         while omxc.poll() == None:
             pass
             #print (mcp.read_adc(0)),"work"
         os.system('xset dpms force off')
         en = str(datetime.now())
         set_localcnt(cn,vid_id)
         up_count(vid_id,st,en)
         print "working"
      else:
          print mcp.read_adc(0)
    except Exception as e:
      print e
      omxc=Popen(['omxplayer','-b',"/home/pi/Rannlab/default.mp4"])
      omxc.wait()
