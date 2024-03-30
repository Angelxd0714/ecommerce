from typing import *
from datetime import *

from pydantic import BaseModel

from ciudades import Ciudades


class Departamentos(BaseModel):
    id:int = None # unique
    nombre:str = None
    ciudades:Ciudades= None
    municipios:int = None