# This is specifically for the middleware in fastapi

from secrets import SECRET_KEY, ALGORITHM
from fastapi import Request, Depends, Header
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.base import BaseHTTPMiddleware
import jwt


class CustomMiddleware(BaseHTTPMiddleware):
    def dispatch(self, request: Request, call_next, jwt_token: str = Header(...),):
        token = request.cookies.get("ac-token")
        if not token:
            return RedirectResponse(url="/login")
        else:
            # Token is present
            try:
                data = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
                if data["exp"] < datetime.datetime.utcnow():
                    return call_next(request)
                else:
                    return RedirectResponse(url="/login")
            except jwt.InvalidSignatureError:
                return RedirectResponse(url="/login")
            
