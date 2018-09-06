import os 
import requests
import json
import uuid
import time
import json
import pymysql
def main():
 try:
   d=[]
   dat = {}
   chk=[]
   date=[]
   def commits(s,d):
    
    if s == '"Success"':
      print "Count Uploaded"  
      db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")  
      cur = db.cursor()
      for i in d:
         sql = "Update counts set issync= 'True' where star ='"+i+"';"
         cur.execute(sql)
      db.commit()
      print "done"
      db.close()
      time.sleep(60)
      main()
    else:
      print "Failed",s
      main()
   db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")  
   cur = db.cursor()
   sql = "Select * from counts where issync = 'False'"
   cur.execute(sql)
   db.close()
   li = cur.fetchall()
   for row in li:
     count = 0
     for r in li:
         if row[0] == r[0]:
            count+=1
     date.append(row[1])
     if row[0] not in chk:
         dat ={"AdsID":row[0],"Count":str(count)}
         d.append(dat)
         chk.append(row[0])
   print d      
   MacId =':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
   data = json.dumps(d)
   print data
   URL1 = "http://smartadvertisement.rannlabprojects.com/CountAds"
   dat = {'MacAddress':MacId,"Count":data}
   print dat
   r = requests.post(url = URL1, data = dat) 
   commits(str(r.text),date)
   
 except Exception as e:
    print e,"up"
    main()
main() 
