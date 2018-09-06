import requests
import json
import os
import uuid
import time
import datetime
MacId =':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
print MacId
while True:
    try:
       #POST (Get YouTube URL based on Gender,Age,Location)
       URL1 = "http://smartadvertisement.rannlabprojects.com/SearchAdvertisement"
       data = {'Gender':'All','Mac':MacId}
       r = requests.post(url = URL1, data = data)
       data1=r.json()
       obj1=json.loads(data1)
       obj_size1 = len(obj1)

       if obj_size1<10:
          obj_size2=len(obj1)
       if obj_size1>=9:
          obj_size2=10
    
       for i in range(0,obj_size2):
         try:
           d1=obj1[i]['VideoUrl']
           exp=obj1[i]['ToDate']
           addedon = obj1[i]['FromDate']
           dd1=obj1[i]['ID']
           cnt = obj1[i]['TotalCounts']
           now = datetime.datetime.now()
           str1=str(dd1)
           path = '/home/pi/Videos/'+str1+'.mp4'
           print path
           if os.path.isfile(path):
                  print "File already present"
                  pass
           else:
                  #Video Download
                  import os
                  from pytube import YouTube
                  try:
                     yt = YouTube(d1)
                     yt.streams.filter(file_extension = "mp4").first().download('/home/pi/Videos',filename = str1)
                     print "Video Downloaded"
                     import pymysql
                     db = pymysql.connect(host="localhost",user="root", passwd="",  db="main")  
                     cur = db.cursor()
                     sql = "Update videos set localcnt = \"1\";"
                     cur.execute(sql)
                     sql = "Insert into videos values (%s,%s,%s,%s,%s,%s)"
                     cur.execute(sql,(dd1,cnt,addedon,exp,now,'0'))
                     db.commit()
                     db.close()

                    
                  except Exception as e :
                      print dd1,"Can't be downloaded",e
                  
         except IndexError:
             print ("Done")
    except ValueError:
         print "No video to download"
    time.sleep(3600)

