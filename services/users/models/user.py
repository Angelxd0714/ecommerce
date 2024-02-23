from typing import *

from models.grupo_rol_permission import GrupoRolPermission

class User:
    id: int = None
    nombre: str = None
    contrasena: str = None
    grupo_id_permiso_roles: List[GrupoRolPermission] = None
    