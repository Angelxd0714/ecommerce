from typing import *
from datetime import *

from pydantic import BaseModel

class Producto(BaseModel):
    id:int = None # unique
    nombre:str = None
    imagen_id: int = None
    det_producto_id:int = None