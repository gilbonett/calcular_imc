from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Charmander:110910@cluster0.3vj7tjx.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['database_imc']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Successfully connected!")
except Exception as e:
    print(e)
