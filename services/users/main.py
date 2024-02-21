from base import *
from functions.rolFunctions import RolFucntions
from functions.userFunctions import UserFunctions
from functions.permissionFunctions import PermissionFunctions
from functions.groupPermissionsFunctions import GroupPermissionFunctions
from services.users.functions.GroupPermissionFunctions import GroupPermissionsPermission



api.add_resource(UserFunctions, '/users','/users/<int:id>',endpoint='users')
api.add_resource(RolFucntions, '/roles', '/roles/<int:id>',endpoint='roles')
api.add_resource(PermissionFunctions, '/permisions', endpoint='permisions')
api.add_resource(GroupPermissionFunctions, '/group_permission','/group_permission/<int:id>', endpoint='group_permission')
api.add_resource(GroupPermissionsPermission,'/permissionsPermission','/permissionsPermission/<int:id>',endpoint='permissionsPermission')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        app.handle_exception(e)