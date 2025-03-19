from pydantic import BaseModel, Field
#modelo conductor
class ModeloConductor(BaseModel):
    Nombre:str = Field(min_length=3),
    TipoLicencia:str = Field(min_length=1,max_length=1,description="Tipo de licencia: A, B, C, D."),
    NumLicencia:str = Field(min_length=12,max_length=12)


