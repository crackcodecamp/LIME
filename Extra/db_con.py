from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://mongodb0.example.net:27017")
db = client.primer
db = client['primer']
db.dataset
db['dataset']
coll = db.dataset
coll = db['dataset']