from typing import *
from datetime import *

from pydantic import BaseModel


class Paypal(BaseModel):
    id: Optional[int]
    email: str
    monto:float