from typing import *
from datetime import *

from pydantic import BaseModel


class Pais(BaseModel):
    id:int = None # unique
    nombre:str = None
    departamento:int = None