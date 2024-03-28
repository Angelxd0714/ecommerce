import threading
from base import *
from functions.rolFunctions import RolFucntions
from functions.userFunctions import UserFunctions
from functions.permissionFunctions import PermissionFunctions
from functions.groupPermissionsFunctions import GroupPermissionFunctions
from services.users.functions.GroupPermissionFunctions import GroupPermissionsPermission
from middleware.handleerros import handle_exception
from functions.groupRolFunctions import GroupRolFunctions
from werkzeug.exceptions import HTTPException

from functions.documentFunctions import TIPO_DOCUMENTOS_FUNCTIONS
from functions.imagenFunctions import IMAGEN_FUNCTIONS
from functions.clientFunctions import ClienteFunction

api.add_resource(UserFunctions, '/users','/users/<int:id>',endpoint='users')
api.add_resource(RolFucntions, '/roles', '/roles/<int:id>',endpoint='roles')
api.add_resource(PermissionFunctions, '/permisions', endpoint='permisions')
api.add_resource(GroupPermissionFunctions, '/group_permission','/group_permission/<int:id>', endpoint='group_permission')
api.add_resource(GroupPermissionsPermission,'/permissionsPermission','/permissionsPermission/<int:id>',endpoint='permissionsPermission')
api.add_resource(GroupRolFunctions, '/group_rol', '/group_rol/<int:id>', endpoint='group_rol')
api.add_resource(TIPO_DOCUMENTOS_FUNCTIONS, '/type_documents', '/type_documents/<int:id>', endpoint='type_documents')
api.add_resource(IMAGEN_FUNCTIONS, '/images', '/images/<int:id>', endpoint='images')
api.add_resource(ClienteFunction, '/clients', '/clients/<int:id>', endpoint='clients')

if __name__ == '__main__':
    try:
        
        app.run(debug=True,threaded=True)
    except HTTPException as e:
         handle_exception(e)