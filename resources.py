# This will contain the complete implementation of the resources

from fastapi import APIRouter, Request, Response
from fastapi.responses import FileResponse
from functions import listDirectory, decryptData, readFile
from secrets import *
from models import AuthData
resource = APIRouter()

def checkPrivileges(resource):
    resource_collection = mongodb["resources"]
    resource = resource_collection.find_one({"book_name": resource})
    if resource:
        # If the resource is present
        level = resource["level"]
        path = resource["resource_path"]
        return (path, level)
    else:
        return (None, None)


@resource.get('/{resource}')
def getResource(resource: str, request: Request):
    resource_path, resource_level = fetchResource(resource)
    if not resource_path or not resource_path:
        # If the resource doesn't exist
        return Response(content=readFile("html/file_not_found.html"), media_type="application/html", status_code=404)
    token = request.cookies.get('ac-token')    
    user  = decryptData(token)
    if user.level >= resource_level:
        # Send him the requested file
        return FileResponse("resources/book1.pdf", media_type="application/pdf", filename=resource)
    else:
        return Response(content=readFile("html/permission_denied.html"), media_type="application/html", status_code=403)

