
#!/usr/bin/python3
 
import pymongo

#mongodb account, database, collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mlp"]
mycol = mydb["first"]
#the whole table
print("the whole information in table first:") 
for x in mycol.find():
  print(x)
print("\n")

#show the information about account_id and picture number
#use find() to search certian word,Set the value of the field to be returned to 1
print("the account id and picture number:")
for x in mycol.find({},{ "_id": 0, "account_id": 1, "picture": 1 }):
  print(x)
print("\n")

#search for a word
myquery = { "keyword": "singer" }
 
mydoc = mycol.find(myquery)
print("the information where keyword is singer:")
for x in mydoc:
  print(x)  
print("\n")

#most popular descriptors
print("the most popular descriptors:")
for x in mycol.find({},{'_id':0,'keyword':1}):
	print(x)
