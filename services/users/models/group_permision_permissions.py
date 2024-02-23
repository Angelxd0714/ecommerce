from typing import *

from models.group_permission import GroupPermission
from models.permission import Permission

class GroupPermissionPermission:
    id: int = None
    grupopermisos_id: List[GroupPermission] = None
    permisos_id: List[Permission] = None