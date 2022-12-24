import pymongo
client = pymongo.MongoClient("mongodb+srv://Akshay:Mongodb1@cluster0.vpuhare.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["myinfo"]
collection = database["akki"]

data = collection.find({"company name" : "ineuron"})
for i in data:
    print(i)