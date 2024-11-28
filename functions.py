# For any other functions

import os
from models import AuthData
from secrets import *

def listDirectory(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return []

def encryptData(data: AuthData) -> str:
    token = crypto_obj.encrypt(bytes(str(data.level)+data.username, 'utf-8'))
    return token

def decryptData(token: str) -> AuthData:
    decrypted_data = crypto_obj.decrypt(token)
    auth = AuthData()
    auth.level = int(decryptData[:1])
    auth.username = decryptData[1:]
    return auth

def readFile(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = file.read()
        return data
    else:
        return ''