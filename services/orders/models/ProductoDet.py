from typing import *
from datetime import *

from pydantic import BaseModel

class DetProducto(BaseModel):
    id:int = None # unique
    descripcion:str = None
    precio: float =  0
    cantidad:int = None
    categoria:int = None