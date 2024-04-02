from typing import *
from datetime import *

from pydantic import BaseModel


class Facturas(BaseModel):
    id:Optional[int]
    cliente_id:int
    fecha_transaccion:date
    paypal_id:int
    tarjetas_id:int
    estado_pago_id:int