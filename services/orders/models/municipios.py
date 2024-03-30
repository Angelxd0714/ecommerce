from typing import *
from datetime import *

from pydantic import BaseModel

class Municipio(BaseModel):
    id:int = None # unique
    nombre:str = None