from fastapi import FastAPI,HTTPException
from typing import Optional,List
from models import modeloUsuario
app = FastAPI(
    title="Mi primer API 192",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)


    

usuarios=[
    {"id":1, "nombre":"Alexis", "edad":21,"correo":"alexis@gmail.com"},
    {"id":2, "nombre":"Jose", "edad":25,"correo":"jose@gmail.com"},
    {"id":3, "nombre":"Maria","edad":27,"correo":"maria@gmail.com"},
    {"id":4, "nombre":"Pedro","edad":23,"correo":"pedrp@gmail.com"}
]

#endpoint home
@app.get("/", tags=["Hola mundo"])

def home():
    return {"hello": "world FastAPI"}

#endpoint consulta todos
@app.get("/todosUsuarios",response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leerUsuarios():
    return usuarios

#endpoint Agregar nuevos usuarios
@app.post("/usuarios/",response_model=modeloUsuario, tags=["Operaciones CRUD"])
def agregarUsuario(usuario: modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return {"El usuario se agregó correctamente": usuario}

#endpoint Actualizar un usuario
@app.put("/usuarios/{id}",response_model=modeloUsuario, tags=["Operaciones CRUD"])
def actualizarUsuario(id: int, usuario: modeloUsuario):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario.model_dump()
            return usuarios[index] 

    raise HTTPException(status_code=400, detail="El usuario no existe")

#endpoint Eliminar un usuario

@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminarUsuario(id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(i)
            return {"El usuario se eliminó correctamente": {"id": id}}
    raise HTTPException(status_code=404, detail="El usuario no existe")