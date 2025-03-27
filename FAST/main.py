from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List, Dict

from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session,Base,engine
from models.modelsDB import User
from routers.usuario import routerUsuario
from routers.auth import routerAuth


app = FastAPI(
    title="Mi primer API 192",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)

app.include_router(routerUsuario)
app.include_router(routerAuth)
Base.metadata.create_all(bind=engine)
    


# endpoint home
@app.get("/", tags=["Hola mundo"])
def home():
    return {"hello": "world FastAPI"}


        

