from typing import *

from models.group_permision_permissions import GroupPermissionPermission
from models.rol import ModelRol

class GrupoRolPermission:
    id:int=None
    grupo_permisos_id:List[GroupPermissionPermission]=None
    rol_id:ModelRol=None
    