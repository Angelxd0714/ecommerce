from typing import *
from datetime import *

from pydantic import BaseModel



class Direccion(BaseModel):
    id:int = None # unique
    calle:str = None
    carrera:str = None
    numero:int = None
    indicador:str = None
    diagonal:str = None
    pais:int = None