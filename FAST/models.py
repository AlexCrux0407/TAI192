from pydantic import BaseModel, Field, EmailStr
#modelo de validaciones
class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0,description="ID único y solo numeros positivos.")
    nombre:str = Field(...,min_length=3,max_length=85,description="Solo letras: Min 3, Máx 85.")
    edad:int = Field(...,gt=0,lt=120,description="Edad entre 0 y 120 años.")
    correo:EmailStr = Field(...,min_length=5,
                       max_length=85,
                       description="Correo electrónico.")

