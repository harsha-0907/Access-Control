#!/bin/python3

from fastapi import FastAPI, APIRouter, Response
from secrets import mongodb, SECRET_KEY, ALGORITHM
from functions import readFile, encryptData
from resources import resource
from custom_middleware import CustomMiddleware
from models import AuthData
import random
import datetime

app = FastAPI()
app.add_middleware(CustomMiddleware)
app.add_api_route("/resource", resource)

@app.get('/login')
def loginPage():
  return Reponse(content=readFile("html/login.html"), media_type="application/html", status_code=200)

@app.post('/login')
def loginUser(response: Response, username: str = Form(...), password: str = Form(...)):
  cred_collection = mongodb["credentials"]
  user = cred_collection.find_one({"username": username})
  db_password = user["password"]; user_level = user["level"]
  if password == db_password:
    auth = AuthData()
    auth.username = username; auth.level = user_level
    payload = {"user_data": random.randint(100000, 999999), "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    headers = {"jwt_token": jwt_token}
    response.content = readFile("html/homePage.html"); response.media_type="application/html"
    response.set_cookie(key="ac-cookie", value=encryptData(auth))
    response.headers = headers
    return response
  else:
    response.content = readFile("html/wrong_credentials.html")
    response.media_type = "application/html"
    response.status_code = 404
    return response
