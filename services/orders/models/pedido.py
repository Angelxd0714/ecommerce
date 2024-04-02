from typing import *
from datetime import *

from pydantic import BaseModel

class Pedido(BaseModel):
    id:int = None # unique
    cantidad:int = None 
    direccion: int = None
    det_pedido:int = None