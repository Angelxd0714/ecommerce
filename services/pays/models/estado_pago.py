from typing import *
from datetime import *

from pydantic import BaseModel
from typing import Optional


class Estado_Pago(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True