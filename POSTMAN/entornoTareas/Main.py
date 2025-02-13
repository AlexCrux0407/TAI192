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
    }
]
