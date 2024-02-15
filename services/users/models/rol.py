from typing import *

class ModelRol:
    id:int=None
    nombre:str=None
    def __init__(self):
        self.id=None
        self.nombre=None
    def __repr__(self):
        return f"Rol(id={self.id}, nombre={self.nombre})"
    