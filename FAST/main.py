from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API 192",
    description="Esto es una descripción de mi API",
    version="1.0.1"
)
usuarios=[
    {"id":1, "nombre":"Alexis", "edad":21},
    {"id":2, "nombre":"Jose", "edad":25},
    {"id":3, "nombre":"Maria","edad":27},
    {"id":4, "nombre":"Pedro","edad":23}
]

#endpoint home
@app.get("/", tags=["Hola mundo"])

def home():
    return {"hello": "world FastAPI"}

#endpoint consulta todos
@app.get("/todosUsuarios", tags=["Operaciones CRUD"])

def leerUsuarios():
    return {"Los usuarios registrados son ": usuarios}

#endpoint Agregar nuevos usuarios
@app.post("/usuarios/", tags=["Operaciones CRUD"])

def agregarUsuario(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario["id"]:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return {"El usuario se agregó correctamente": usuario}

#endpoint Actualizar un usuario
@app.put("/usuarios/{id}", tags=["Operaciones CRUD"])

def actualizarUsuario(id: int, usuario: dict):
    for usr in usuarios:
        if usr["id"] == id:
            for key, value in usuario.items():
                usr[key] = value
            return {"El usuario se actualizó correctamente": usr}
    raise HTTPException(status_code=404, detail="El usuario no existe")

#endpoint Eliminar un usuario

@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminarUsuario(id: int):
    for i, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(i)
            return {"El usuario se eliminó correctamente": {"id": id}}
    raise HTTPException(status_code=404, detail="El usuario no existe")