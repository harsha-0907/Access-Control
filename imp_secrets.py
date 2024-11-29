from cryptography.fernet import Fernet
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# MongoDB
db_password = "PASSWORD"
mongo_url = f"mongodb+srv://root:{db_password}@cluster0.9podb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongodb = MongoClient(mongo_url, server_api=ServerApi('1'))["access-control"]
# print(mongodb)
# Cryptography
key = "CRYPTOGRAPHIC_KEY"
crypto_obj = Fernet(key)
# JWT Token
SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"