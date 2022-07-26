from pymongo import MongoClient
client = MongoClient("mongodb://root-crashell:password-crashell@localhost:27017")
db = client.db
try:
    db.command("serverStatus")
except Exception as e:
    print(e)
else:
    print("You are connected!")

client.close()