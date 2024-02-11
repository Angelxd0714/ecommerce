from typing import *
from datetime import *
class Client:
    id: int = None
    nombre: str = None
    apellido: str = None
    telefono: int = None
    email: str = None
    celular: int = None
    direccion: str = None
    fechaNacimiento:Union[date,None] = None
