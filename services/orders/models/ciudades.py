from typing import *
from datetime import *

from pydantic import BaseModel

class Ciudades(BaseModel):
    id:int = None # unique
    nombre:str = None