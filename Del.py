import json
import requests
import time
import os

while True:
  try:
     da = []
     URL = "http://smartadvertisement.rannlabprojects.com/SelectExpiredCampaign" 
     PARAMS ={}
     r = requests.post(url = URL , params = PARAMS)
     data =  r.json()
     try:
        d = json.loads(data)
     except:
        print "no data"
     for dat in d:
       s= str(dat.get("ID"))
       da.append(s)
     print da
     for name in da:
       try:  
         os.remove("/home/pi/Videos/"+name+".mp4")
         import pymysql
         db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")  
         cur = db.cursor()
         sql = "Delete from videos where id = %s;"
         cur.execute(sql,(name))
       except:
         print "No data to delete"
     URL = "http://smartadvertisement.rannlabprojects.com/DeleteExpiredCampaign"
     PARAMS ={}
     r = requests.post(url = URL , params = PARAMS)
     print " delete done"
  except Exception as e:
   pass
  time.sleep(3600)

