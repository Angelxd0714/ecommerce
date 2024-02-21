from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from flask import jsonify, request
from base import * 
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import USUARIOS
dataBase = db

class UserFunctions(Resource):
    
    
    def __init__(self,db:SQLAlchemy=dataBase):
        """
        Initialize the class with the database object.

        Args:
            db (SQLAlchemy): The database object to be used for the operations.
        """
        self.db = db
    def get(self,id:int=None):
        """Get a user or a list of users.

        Args:
            id (int, optional): The ID of the user to retrieve. If not provided,
                a list of all users will be returned.

        Returns:
            A JSON object containing the user information, or a list of users if
            no ID was provided.
        """
        if id is None:
            return self.get_all()
        else:
            return self.get_single(id)
    def get_single(self, id:int):
        """Get a single user.

        Args:
            id (int): The ID of the user to retrieve.

        Returns:
            A JSON object containing the user information, or a 404 error if the user
            was not found.
        """
        user:User = self.db.session.query(USUARIOS).get(id)
        if not user:
            return jsonify({'message': 'User not found'})
        return jsonify({"id": user.id, "nombre": user.nombre, "contrasena": user.contrasena,'grupo_id_permiso_roles':user.grupo_id_permiso_roles})
    def get_all(self):
        query = self.db.session.query(USUARIOS).all()
        if not query:
            return jsonify({'message': 'Users not found'})
        dict_users = [{"id": user.id, "nombre": user.nombre, "contrasena": user.contrasena,'grupo_id_permiso_roles':user.grupo_id_permiso_roles} for user in query]
        return jsonify({"users": dict_users})
    def post(self):
        data=request.get_json()
        user=USUARIOS(nombre=data['nombre'], contrasena=data['contrasena'],grupo_id_permiso_roles=data['grupo_id_permiso'])
        self.db.session.add(user)
        self.db.session.commit()
        return jsonify({'message':'User created'})

    def put(self,id:int):
        user=self.db.session.query(USUARIOS).get(id)
        if not user:
            return jsonify({'message':'User not found'})
        data:User=request.get_json()
        user.nombre=data['nombre']
        user.contrasena=data['contrasena']
        user.grupo_id_permiso_roles=data['grupo_id_permiso']
        self.db.session.commit()
        return jsonify({'message':'User updated'})

    def delete(self,id:int):
        user=self.db.session.query(USUARIOS).get(id)
        if not user:
            return jsonify({'message':'User not found'})
        self.db.session.delete(user)
        self.db.session.commit()
        return jsonify({'message':'User deleted'})
