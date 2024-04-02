from typing import *
from datetime import *

from pydantic import BaseModel




class Departamentos(BaseModel):
    id:int = None # unique
    nombre:str = None
    ciudades:int= None
    municipios:int = None