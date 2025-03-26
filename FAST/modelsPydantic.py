from pydantic import BaseModel, Field, EmailStr
#modelo de validaciones
class modeloUsuario(BaseModel):
    name:str = Field(...,min_length=3,max_length=85,description="Solo letras: Min 3, Máx 85.")
    age:int = Field(...,gt=0,lt=120,description="Edad entre 0 y 120 años.")
    email:EmailStr = Field(...,min_length=5,
                       max_length=85,
                       description="email electrónico.")

class modeloAuth(BaseModel):
    email:EmailStr = Field(...,min_length=5,
                       max_length=85,
                       description="email electrónico.")
    passw:str = Field(..., min_length=8, strip_whitespace = True, description="Contraseña: Min 8 caracteres.")