from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from base import * 

dataBase = db

class UserFunctions(Resource):
    
    def __init__(self,db:SQLAlchemy=dataBase):
        self.db = db
    def get(self):
        
        return {'message': 'Hello World'}

    def post(self):
        return {'message': 'Hello World'}

    def put(self):
        return {'message': 'Hello World'}

    def delete(self):
        return {'message': 'Hello World'}
