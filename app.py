import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['apple']
collection = database['fruits']

fruits = [fruit for fruit in collection.find({})]

print(fruits)

  

 
