from flask_restful import Resource

from services.users.models.user import User

class UserFunctions(Resource):
    def get(self):
        return {'message': 'Hello World'}

    def post(self,user:User):
        return {'message': 'Hello World'}

    def put(self,user:User.id):
        return {'message': 'Hello World'}

    def delete(self):
        return {'message': 'Hello World'}
