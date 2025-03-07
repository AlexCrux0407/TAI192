from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict

from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT

app = FastAPI(
    title="Mi primer API 192",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "Alexis", "edad": 21, "correo": "alexis@gmail.com"},
    {"id": 2, "nombre": "Jose", "edad": 25, "correo": "jose@gmail.com"},
    {"id": 3, "nombre": "Maria", "edad": 27, "correo": "maria@gmail.com"},
    {"id": 4, "nombre": "Pedro", "edad": 23, "correo": "pedrp@gmail.com"}
]

# endpoint home
@app.get("/", tags=["Hola mundo"])
def home():
    return {"hello": "world FastAPI"}

# endpoint consulta todos
@app.get("/todosUsuariox", dependencies=[Depends(BearerJWT())], response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leerUsuarios():
    return usuarios

# endpoint Agregar nuevos usuarios
@app.post("/usuarios/", dependencies=[Depends(BearerJWT())], response_model=modeloUsuario, tags=["Operaciones CRUD"])
def agregarUsuario(usuario: modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario.model_dump())
    return usuario

# endpoint Actualizar un usuario
@app.put("/usuarios/{id}", dependencies=[Depends(BearerJWT())], response_model=modeloUsuario, tags=["Operaciones CRUD"])
def actualizarUsuario(id: int, usuario: modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario.model_dump()
            return usuarios[index]

    raise HTTPException(status_code=400, detail="El usuario no existe")

# endpoint Eliminar un usuario
@app.delete("/usuarios/{id}", dependencies=[Depends(BearerJWT())], tags=["Operaciones CRUD"])
def eliminarUsuario(id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(i)
            return {"El usuario se eliminó correctamente": {"id": id}}
    raise HTTPException(status_code=404, detail="El usuario no existe")

# endpoint autenticacion
@app.post("/auth", tags=["Autentificación"])
def login(autorizacion: modeloAuth):
    if autorizacion.correo == "alexis@gmail.com" and autorizacion.passw == "admin123":
        token: str = createToken(autorizacion.model_dump())
        print(token)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Usuario sin acceso")