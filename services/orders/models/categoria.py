from typing import *
from datetime import *

from pydantic import BaseModel

class Categoria(BaseModel):
    id:Optional[int] = None # unique
    nombre:Optional[str]=None 
    