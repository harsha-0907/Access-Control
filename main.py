#!/bin/python3

from fastapi import FastAPI, APIRouter, Response, Form
from fastapi.responses import RedirectResponse
from imp_secrets import mongodb, SECRET_KEY, ALGORITHM
from functions import readFile, encryptData
from resources import resource
from models import AuthData
import random
import jwt
import datetime

app = FastAPI()
app.include_router(resource, prefix="/resource")

@app.get('/')
def homePage():
  return RedirectResponse("/login")

@app.get('/login')
def loginPage():
  return Response(content=readFile("html/login.html"), media_type="text/html", status_code=200)

@app.post('/login')
def loginUser(username: str = Form(...), password: str = Form(...)):
  cred_collection = mongodb["credentials"]
  user = cred_collection.find_one({"username": username})
  db_password = user["password"]; user_level = user["level"]
  if password == db_password:
    auth = AuthData(username=username, level=user_level)
    payload = {"user_data": random.randint(100000, 999999), "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    response = Response(content=readFile("html/homePage.html"), media_type="text/html", headers={"jwt_token": jwt_token}, status_code=200)
    ac_token = encryptData(auth).decode('utf-8')
    response.set_cookie(key="ac-token", value=ac_token)
    print(ac_token)
    return response
  else:
    # Wrong Credential
    return Response(content=fileRead("html/wrong_credentials.html"), media_type="text/html", status_code=404)

@app.get()
