from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Gestor de tareas",
    description="API para administrar tareas",
    version="1.0.0"
)

tareas = [
    {
        "id": 1,
        "titulo": "Entrega Moya",
        "descripcion": "Entregar la tarea de Moya",
        "vencimiento": "12/02/2025",
        "estado": "pendiente"
    },
    {
        "id": 2,
        "titulo": "Entrega Pons",
        "descripcion": "Entregar la tarea de Pons",
        "vencimiento": "15/02/2025",
        "estado": "pendiente"
    }
]

#mostar tareas
@app.get("/tareas", tags=["tareas"])
def mostrarTareas():
    return {"Las tareas registradas son": tareas}

#buscar tarea por ID
@app.get("/tareas/{id}", tags=["tareas"])

def buscarTarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#crear tarea
@app.post("/tareas", tags=["tareas"])
def crearTarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea["id"]:
            raise HTTPException(status_code=400, detail="El ID de tarea ya existe")
    tareas.append(tarea)
    return {"La tarea se creó correctamente": tarea}
