from fastapi import FastAPI
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

#endpoint promedio
@app.get("/promedio", tags=["Mi calificacion TAI"])
def promedio():
    return 10.36

#endpoint usuario
@app.get("/usuario/{id}", tags=["Parametro obligatorio"])
def consultausuario(id:int):
    return{"Se encontró el usuario": id}

#endpoint parametro opcional
@app.get("/usuario/", tags=["Parametro opcional"])
def consultausuario2(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"mensaje": "Se encontró el usuario", "usuario": usu}
        return {"mensaje": f"No se encontró el usuario con id: {id}"}
    else:
        return {"mensaje": "No se proporcionó un ID"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}