from typing import *

class User:
    id: int = None
    nombre: str = None
    contrasena: str = None
    grupo_id_permiso_roles: List[int] = None
    