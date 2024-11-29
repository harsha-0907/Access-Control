# The complete implementation of the login page

from fastapi import Response, APIRouter, Form
from imp_secrets import *
from functions import readFile, encryptData
from models import AuthData
import jwt
import datetime
import random

login_router = APIRouter()

@login_router.get('/')
def loginPage():
  return Response(content=readFile("html/login.html"), media_type="text/html", status_code=200)

@login_router.post('/')
def loginUser(username: str = Form(...), password: str = Form(...)):
  cred_collection = mongodb["credentials"]
  user = cred_collection.find_one({"username": username})
  db_password = user["password"]; user_level = int(user["level"])
  if password == db_password:
    auth = AuthData(username=username, level=user_level)
    payload = {"user_data": random.randint(100000, 999999), "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    if user["level"] == 4:
      # This is the admin
      response = Response(content=readFile("html/admin_homePage.html"), media_type="text/html", headers={"jwt_token": jwt_token}, status_code=200)
      ac_token = encryptData(auth)
      response.set_cookie(key="ac-token", value=ac_token)
      # print(ac_token)
      return response
    else:
      response = Response(content=readFile("html/homePage.html"), media_type="text/html", headers={"jwt_token": jwt_token}, status_code=200)
      ac_token = encryptData(auth)
      response.set_cookie(key="ac-token", value=ac_token)
      # print(ac_token)
      return response
  else:
    # Wrong Credentials
    return Response(content=fileRead("html/wrong_credentials.html"), media_type="text/html", status_code=404)
