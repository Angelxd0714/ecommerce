from base import *
from functions.rolFunctions import RolFucntions
from functions.userFunctions import UserFunctions
api.add_resource(UserFunctions, '/users')
api.add_resource(RolFucntions, '/roles', '/roles/<int:id>',endpoint='roles')

if __name__ == '__main__':
    app.run(debug=True)