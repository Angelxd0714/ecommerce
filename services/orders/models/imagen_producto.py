from typing import *
from datetime import *

from pydantic import BaseModel

class ImagenProducto(BaseModel):
    id:int = None
    url:str = None