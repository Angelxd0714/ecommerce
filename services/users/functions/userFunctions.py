from flask_restful import Resource,http_status_message
from flask_sqlalchemy import SQLAlchemy

from models.user import User
from flask import jsonify, request
from base import * 
from middleware.handleerros import handle_exception, not_found, server_error
from sqlalchemy.exc import *
import sys
from utils.expression import validate_pass
from utils.encrypt import generate_encrypted_password
sys.path.append('/home/angel/Documents/ecommerce/')
from services.users.middleware.authentication import auth_required
from config.models import USUARIOS
dataBase = db

class UserFunctions(Resource):
    
    
    def __init__(self,db:SQLAlchemy=dataBase):
        self.status=None
        """
        Initialize the class with the database object.

        Args:
            db (SQLAlchemy): The database object to be used for the operations.
        """
        self.db = db
    @auth_required("view")    
    def get(self,id:int=None)->dict:
        """Get a user or a list of users.

        Args:
            id (int, optional): The ID of the user to retrieve. If not provided,
                a list of all users will be returned.

        Returns:
            A JSON object containing the user information, or a list of users if
            no ID was provided.
        """
        try:
            if id is None:
                return self.get_all()
            else:
                return self.get_single(id)
        except Exception as specific_error:
            return handle_exception(404, f'Error: {specific_error}')
    def get_single(self, id:int):
        """Get a single user.
        
        Args:
            id (int): The ID of the user to retrieve.

        Returns:
            A JSON object containing the user information, or a 404 error if the user
            was not found.
        """
        try:
            user:User = self.db.session.query(USUARIOS).get(id)
            
            if not user:
                self.status = http_status_message(404)
                return jsonify({'status':self.status})
            self.status = http_status_message(200)
            return jsonify({"id": user.id, "nombre": user.nombre, "contrasena": user.contrasena,'grupo_rol_permisos_id':user.grupo_rol_permisos_id,'status':self.status})
        except Exception as specific_error:
            return handle_exception(500, f'Error: {specific_error}')
    def get_all(self):
        try:
            query = self.db.session.query(USUARIOS).all()
            if not query:
                self.status = http_status_message(404)
                return jsonify({'status': self.status})
            dict_users = [{"id": user.id, "nombre": user.nombre, "contrasena": user.contrasena,'grupo_rol_permisos_id':user.grupo_rol_permisos_id} for user in query]
            self.status = http_status_message(200)
            return jsonify({"users": dict_users, "status":self.status})
        except Exception as specific_error:
            return handle_exception(500, f'Error: {specific_error}')

    @auth_required("insert")        
    def post(self):
        try:
            
            data=request.get_json()
            
            if isinstance(data['nombre'],int):
                return jsonify({'message':'El nombre no puede ser un numero!'})
            elif validate_pass(data['contrasena']) is False:
                return jsonify({'message':'La contraseña debe tener al menos 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula y al menos un dígito!'})   
            elif isinstance(data['grupo_rol_permisos_id'], str):
                return jsonify({'message':'El grupo_rol_permisos_id no puede ser un una letra!'})
            encrypt = generate_encrypted_password(data['contrasena'])
            user=USUARIOS(nombre=data['nombre'], contrasena=encrypt,grupo_rol_permisos_id=data['grupo_rol_permisos_id'])
            self.db.session.add(user)
            self.db.session.commit()
            self.status = http_status_message(201)
            return jsonify({'status':self.status})
        except Exception as specific_error:
        
            return server_error(specific_error)
    @auth_required("update")
    def put(self,id:int):
            try:
                user = self.db.session.query(USUARIOS).filter(USUARIOS.id == id).first()
                if not user:
                    self.status = http_status_message(404)
                    return jsonify({'status': self.status})
                data = request.get_json()
                if data.get('nombre'):
                    user.nombre = data['nombre']
                # Actualizar el campo 'contrasena' si está presente en los datos
                if data.get('contrasena'):
                    user.contrasena = data['contrasena']
                # Actualizar el campo 'grupo_rol_permisos_id' si está presente en los datos
                if data.get('grupo_rol_permisos_id'):
                    user.grupo_rol_permisos_id = data['grupo_rol_permisos_id']
                self.db.session.commit()
                self.status = http_status_message(201)
                return jsonify({'message': 'User updated'})
            except Exception as specific_error:
                mensaje = str(specific_error)
                return jsonify({'message':mensaje})
    @auth_required("delete")
    def delete(self,id:int):
        try:
            user=self.db.session.query(USUARIOS).get(id)
            if not user:
                return jsonify({'message':'User not found'})
            self.db.session.delete(user)
            self.db.session.commit()
            return jsonify({'message':'User deleted'})
        except IntegrityError as specific_error:
            return handle_exception(specific_error)
        except Exception as specific_error:
            return not_found(specific_error)
