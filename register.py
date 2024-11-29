# The complete implementation of the register router

from fastapi import APIRouter, Response, Request, Form
from functions import readFile, decryptData
from imp_secrets import mongodb

register_router = APIRouter()

@register_router.get('/')
def getRegistrationPage(request: Request):
    # This will only be available to the Admins
    ac_token = request.cookies.get("ac-token")
    user_data = decryptData(ac_token)
    if user_data.level == 4:
        return Response(content=readFile("html/register.html"), media_type="text/html", status_code=200)
    else:
        return Response(content=readFile("html/file_not_found.html"), media_type="text/html", status_code=404)


@register_router.post("/")
def registerUser(request: Request, username: str = Form(...), password: str = Form(...), level: int = Form(...)):
    # This will only be available to the admin
    ac_token = request.cookies.get("ac-token")
    user_data = decryptData(ac_token)
    if user_data.level == 4:
        credential_collections = mongodb["credentials"]
        # Check if the username is already taken
        if credential_collections.find_one({"username": username}):
            return Response(content=readFile("html/username_taken.html"), media_type="text/html", status_code=200)
        else:
            credential_collections = mongodb["credentials"]
            credential_collections.insert_one({"username": username, "level": level, "password": password})
            return Response(content=readFile("html/created_user.html"), media_type="text/html", status_code=200)
    else:
        return Response(content=readFile("html/file_not_found.html"), media_type="text/html", status_code=404)


