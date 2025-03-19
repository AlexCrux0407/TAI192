from fastapi import FastAPI, HTTPException, Depends
from modelsPydantic import ModeloConductor
from typing import List


conductores = [{"Nombre": "Julio","TipoLicencia": "A","NumLicencia" : "123456789012"},
     {"Nombre": "Juan","TipoLicencia": "B","NumLicencia" : "987654321098"},
     {"Nombre": "Pedro","TipoLicencia": "C","NumLicencia" : "456789123045"},
     {"Nombre": "Ana","TipoLicencia": "D","NumLicencia" : "789123426078"}]

app = FastAPI()

@app.get("/mostrar",response_model=List[ModeloConductor], tags=["Mostrar conductores"])
def mostrar_conductores():
    return conductores


@app.get("/consulta/{NumLicencia}",response_model=List[ModeloConductor], tags=["Consulta por licencia"])
def get_conductor(NumLicencia: str):
    for i in conductores:
        if i["NumLicencia"] == NumLicencia:
            return i
    raise HTTPException(status_code=404, detail="Conductor no encontrado")

@app.delete("/delete/{NumLicencia}", tags=["Eliminar conductor"])
def delete_conductor(NumLicencia: str):
    for i in range(len(conductores)):
        if conductores[i]["NumLicencia"] == NumLicencia:
            del conductores[i]
            return {"Conductor eliminado"}
    raise HTTPException(status_code=404, detail="Conductor no encontrado")