from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
import uvicorn
import logging
import auth
from models.user import User

app = FastAPI(title='Dialoger-Auth')
PORT = 1211

log = logging.getLogger(__name__)

class App:
    @app.get('/')
    async def docs(self: Request):
        return RedirectResponse(f'{self.url}docs')
    
    @app.post('/auth')
    async def login(self: Request, user = Depends(auth.verify)):
        return HTTPException(200) 

    @app.post('/register')
    async def register(self: Request, user: User):
        if auth.register(username=user.username, password=user.password):
            return HTTPException(200)
        
    @app.post('/login')
    async def register(self: Request, user: User):
        if auth.login(username=user.username, password=user.password):
            return HTTPException(200)

    @staticmethod
    def init():
        log.info('Dialoger-Auth Service is starting...')
        uvicorn.run(app, port=PORT)