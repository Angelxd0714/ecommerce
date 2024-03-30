from typing import *
from datetime import *

from pydantic import BaseModel

class Pedido(BaseModel):
    id:int = None # unique
    cantidad:str = None | 0
    direccion: int = None
    det_pedido:int = None