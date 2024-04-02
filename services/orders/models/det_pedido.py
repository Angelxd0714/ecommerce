from typing import *
from datetime import *

from pydantic import BaseModel

class DetPedido(BaseModel):
    id:int = None # unique
    producto_id: int = None
    fecha_pedido: date = None
    cliente_id: int = None