#!/bin/python3

from fastapi import FastAPI, APIRouter, Response, Form
from fastapi.responses import RedirectResponse
from resources import resource
from register import register_router
from login import login_router

app = FastAPI()
app.include_router(resource, prefix="/resource")
app.include_router(register_router, prefix="/register")
app.include_router(login_router, prefix="/login")

@app.get('/')
def homePage():
  return RedirectResponse("/login")
