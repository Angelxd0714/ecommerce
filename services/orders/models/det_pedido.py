from typing import *
from datetime import *

from psycopg2 import Date
from pydantic import BaseModel

class DetPedido(BaseModel):
    id:int = None # unique
    cantidad:str = None | 0
    producto_id: int = None
    fecha_pedido: Date = None
    cliente_id: int = None