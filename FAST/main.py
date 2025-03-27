from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List, Dict

from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session,Base,engine
from models.modelsDB import User

app = FastAPI(
    title="Mi primer API 192",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)
    
usuarios = [
    {"id": 1, "nombre": "Alexis", "edad": 21, "email": "alexis@gmail.com"},
    {"id": 2, "nombre": "Jose", "edad": 25, "email": "jose@gmail.com"},
    {"id": 3, "nombre": "Maria", "edad": 27, "email": "maria@gmail.com"},
    {"id": 4, "nombre": "Pedro", "edad": 23, "email": "pedrp@gmail.com"}
]

# endpoint home
@app.get("/", tags=["Hola mundo"])
def home():
    return {"hello": "world FastAPI"}

# endpoint consulta todos
@app.get("/todosUsuarios", response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leerUsuarios():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message":"error al consultar usuarios","Excepcion": str(e)})
    finally:
        db.close()

#endpoint buscar por id
@app.get("/usuarios/{id}", response_model=modeloUsuario, tags=["Operaciones CRUD"])
def leerUsuario(id: int):
    db = Session()
    try:
        consultauno = db.query(User).filter(User.id == id).first()
        if not consultauno:
            return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consultauno))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message":"error al consultar usuario","Excepcion": str(e)})
    finally:
        db.close()
        
        
# endpoint Agregar nuevos usuarios
@app.post("/usuarios/", response_model=modeloUsuario, tags=["Operaciones CRUD"])
def agregarUsuario(usuario: modeloUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse (status_code=201, content={"message": "Usuario creado correctamente", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message":"error al guardar usuario","Excepcion": str(e)})
    finally:
        db.close()

# endpoint Actualizar un usuario
@app.put("/usuarios/{id}", response_model=modeloUsuario, tags=["Operaciones CRUD"])
def actualizarUsuario(id: int, usuario: modeloUsuario):
    db = Session()
    try:
        consultados = db.query(User).filter(User.id == id).first()
        if not consultados:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})        
        for key, value in usuario.model_dump().items():
            setattr(consultados, key, value)
            return JSONResponse(status_code=200, content={"message": "Usuario actualizado correctamente", "usuario": usuario.model_dump()})        
        db.commit()
        db.refresh(consultados) 
        return JSONResponse(content=jsonable_encoder(consultados))
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "error al actualizar usuario", "Excepcion": str(e)})
    finally:
        db.close()

# endpoint Eliminar un usuario
@app.delete("/usuarios/{id}", response_model=Dict[str, str], tags=["Operaciones CRUD"])
def eliminarUsuario(id: int):
    db = Session()
    try:
        consultatres = db.query(User).filter(User.id == id).first()
        if not consultatres:
            return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})        
        db.delete(consultatres)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado correctamente"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "error al eliminar usuario", "Excepcion": str(e)})
    finally:
        db.close()
        
# endpoint autenticacion
@app.post("/auth", tags=["Autentificación"])
def login(autorizacion: modeloAuth):
    if autorizacion.email == "alexis@gmail.com" and autorizacion.passw == "admin123":
        token: str = createToken(autorizacion.model_dump())
        print(token)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Usuario sin acceso")
