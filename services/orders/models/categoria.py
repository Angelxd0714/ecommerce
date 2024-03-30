from typing import *
from datetime import *

from pydantic import BaseModel

class Pedido(BaseModel):
    id:int = None # unique
    nombre:str = None
    