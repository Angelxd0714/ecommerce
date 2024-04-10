from pydantic import BaseModel

class Permiso(BaseModel):
    permiso:str

class Permisos(BaseModel):
    permisos:list[Permiso]