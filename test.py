import pymongo
client = pymongo.MongoClient("mongodb+srv://Akshay:Akshaydesai876@cluster0.vpuhare.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name" : "akshay",
    "email" : "akshay@gmail.com",
    "surname" : "desai"
}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)