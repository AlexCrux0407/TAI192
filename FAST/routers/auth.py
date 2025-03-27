from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List, Dict

from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session,Base,engine
from models.modelsDB import User
from fastapi import APIRouter


routerAuth = APIRouter()

# endpoint autenticacion
@routerAuth.post("/auth", tags=["Autentificación"])
def login(autorizacion: modeloAuth):
    if autorizacion.email == "alexis@gmail.com" and autorizacion.passw == "admin123":
        token: str = createToken(autorizacion.model_dump())
        print(token)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Usuario sin acceso")