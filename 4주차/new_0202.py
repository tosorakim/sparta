from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)