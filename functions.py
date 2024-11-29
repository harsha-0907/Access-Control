# For any other functions

import os
from models import AuthData
from imp_secrets import *

def listDirectory(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        return []

def encryptData(data: AuthData) -> str:
    token = crypto_obj.encrypt(bytes(str(data.level)+data.username, 'utf-8'))
    return token.decode('utf-8')

def decryptData(token: str) -> AuthData:
    try:
        decrypted_data = crypto_obj.decrypt(token).decode('utf-8')
        auth = AuthData(username=decrypted_data[1:], level=int(decrypted_data[0]))
        print(auth.username, auth.level)
        return auth
    except Exception as e:
        print("error: ", e)
        return dict()

def readFile(path):
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                data = file.read()
            return data
        else:
            return ''
    except Exception as e:
        print("Error Reading File : ", e)
        return ''

def removeExtension(name: str):
    return name[:name.find('.')]

def trimFile(name):
    return removeExtension(name).capitalize()

