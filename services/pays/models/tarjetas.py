from typing import *
from datetime import *

from pydantic import BaseModel
from datetime import date



class Tarjetas(BaseModel):
    id:int = None
    numero:int = None
    fecha_vencimiento:date = None
    cvv:int = None
    monto:float = None