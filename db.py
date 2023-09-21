from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Charmander:110910@cluster0.3vj7tjx.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['database_imc']
print(db)

colecao = db['dados_imc']
usuario = {"nome": "Pedro", "peso": "70", "altura": "1.62"}
busca = colecao.find_one()
print(busca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Estamos conectados no MongoDB!")
except Exception as e:
    print(e)
