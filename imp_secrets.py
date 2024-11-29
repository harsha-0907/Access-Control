from cryptography.fernet import Fernet
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB
db_password = "jum32J"
mongo_url = f"mongodb+srv://root:{db_password}@cluster0.9podb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongodb = MongoClient(mongo_url, server_api=ServerApi('1'))["access-control"]
# print(mongodb)
# Cryptography
key = "WZm7FxTS8sY2OrjYaZwEUu1aUAIpUVW_1JErpUS0lXY="
crypto_obj = Fernet(key)

# JWT Token
SECRET_KEY = "LKJDFUEWUDFBHDF"
ALGORITHM = "HS256"