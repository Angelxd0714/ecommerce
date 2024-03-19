from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
import sys

from generate_token.token import generate_token
from services.auth.redis.redis import set_token
from services.auth.send_message import callback

sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import CLIENTES,TIPO_DE_DOCUMENTO,IMAGEN_USUARIO,USUARIOS
from base import * 

database = db

class Login(Resource):
    def __init__(self,db:SQLAlchemy=database):
        self.db = db
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('correo', type=str, required=True)
        parser.add_argument('contrasena', type=str, required=True)
        args = parser.parse_args()
        correo = self.db.session.query(CLIENTES,USUARIOS).join(USUARIOS,CLIENTES.usuarios_id==USUARIOS.id).filter(CLIENTES.email == args['correo']).first()
        if correo is None:
            return {'message': 'Usuario no encontrado o correo no existente'}, 404
        if  not check_password_hash(correo[1].contrasena, args['contrasena']):
            return {'message': 'Contraseña incorrecta'}, 404
        else:
            token = generate_token({'id': correo[0].cliente_id, 'correo': correo[0].email})
            callback(body=token)
            return {'token': token}, 200
            