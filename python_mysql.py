#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
db = pymysql.connect("localhost", "root", "1996711", "mlp", charset='utf8' )

# use cursor() to get action cursor 
cursor = db.cursor()

# use execute to SQL
cursor.execute("select VERSION()")

# use fetchone() gain data
data = cursor.fetchone()

print ("Database version : %s " % data)

#the whole results of the table
sql="select * from first"
try:
	cursor.execute(sql) 	#run sql sentence
	results = cursor.fetchall()	#fetch all results
	print('The whole results is:')
	print(results)
	print('\n')
except:
   print ("Error: unable to fecth data")

#search for keyword
sql = "select * from first where keyword='singer,celebrity'" 
try:
   # execute sql
   cursor.execute(sql)
   # Get a list of all records
   results = cursor.fetchall()
   print("details where keyword=singer,celebrity" )

   for row in results:
      user = row[0]
      account = row[1]
      picture = row[2]
      pic_location = row[3]
      sex = row[4]
      videotime = row[5]
      keyword = row[6]
      # print result
      print (("user=%s,account=%s,picture=%s,pic_location=%s,sex=%s,videotime=%s,keyword=%s") % \
             (user, account, picture, pic_location,sex,videotime,keyword ))
      print("\n")
except:
   print ("Error: unable to fecth data")


#number of picture
sql="select * from first"

try:
    cursor.execute(sql) 	
    results = cursor.fetchall()
    print("number of picture")
    for row in results:
        user = row[0]
        account = row[1]
        picture = row[2]
        pic_location = row[3]
        sex = row[4]
        videotime = row[5]
        keyword = row[6]
        print(("user=%s,account=%s,picture=%s") % \
        (user,account,picture))
    print("\n")    
except:
   print ("Error: unable to fecth data")

# most popular descriptors
sql="select keyword,count(*) as count from first group by keyword order by count desc"
try:
	cursor.execute(sql) 	
	results = cursor.fetchall()
	print('the most popular description:')
	print(results)
	print("\n")

except:
   print ("Error: unable to fecth data")









# close database
db.close()
