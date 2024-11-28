from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    level: int
    jwt: str
    token: str

class Admin(BaseModel):
    username : str = "admin"
    password: str = "P@ssword123"
    jwt: str
    token: str
    def changeAccess(user: User, level):
        user.level = level
    
    def updateDB(username, field, value):
        # Contains logic to change particular field of a db document
        return True

class Resources(BaseModel):
    name: str
    level: int
    location: str

class AuthData(BaseModel):
    username: str
    level: int