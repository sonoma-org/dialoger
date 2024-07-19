from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from database import DataBase


security = HTTPBasic()

def verify(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not DataBase().get_user(credentials.username, credentials.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return credentials.username
    
def register(username: str, password: str):
    if not DataBase().register_user(username, password):
        raise HTTPException(
            status_code=409,
            detail="Duplicate username",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return True
    
def login(username: str, password: str):
    if not DataBase().get_user(username, password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return True