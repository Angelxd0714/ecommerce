from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
import sys
import time
from generate_token.token import generate_token
from services.auth.redis.redis import set_token
from services.auth.send_message import callback

sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import GRUPOPERMISOS_PERMISOS,GRUPO_DE_PERMISOS,PERMISOS,USUARIOS,CLIENTES,GRUPO_ROL_PERMISOS,ROl
from base import * 

database = db



class Login(Resource):

    
    time = 1800 + int(time.time())
    def __init__(self,db:SQLAlchemy=database):
        self.db = db
        
    def post(self):
        """
         Valida el usuario y la contraseña
         Args:
             correo (str): Correo del usuario
             contrasena (str): Contraseña del usuario
             Returns:
                 JSON: A JSON object containing the user data.
        
        """
        parser = reqparse.RequestParser()
        parser.add_argument('correo', type=str, required=True)
        parser.add_argument('contrasena', type=str, required=True)
        args = parser.parse_args()
        correo = self.db.session.query(CLIENTES, USUARIOS, PERMISOS.nombre, GRUPO_DE_PERMISOS)\
        .join(USUARIOS, CLIENTES.usuarios_id == USUARIOS.id)\
        .join(GRUPO_ROL_PERMISOS, GRUPO_ROL_PERMISOS.id == USUARIOS.grupo_rol_permisos_id)\
        .join(GRUPOPERMISOS_PERMISOS, GRUPOPERMISOS_PERMISOS.id == GRUPO_ROL_PERMISOS.gruporol_id)\
        .join(GRUPO_DE_PERMISOS, GRUPOPERMISOS_PERMISOS.grupopermisos_id == GRUPO_DE_PERMISOS.id)\
        .join(PERMISOS, GRUPOPERMISOS_PERMISOS.permisos_id == PERMISOS.id)\
        .filter(CLIENTES.email == args['correo']).first()

        if correo is None:
            return {'message': 'Usuario no encontrado o correo no existente'}, 404
        
        if not check_password_hash(correo[1].contrasena, args['contrasena']):
            return {'message': 'Contraseña incorrecta'}, 404
        
        # Obtener los permisos asociados al grupo
        grupo_permisos = self.db.session.query(GRUPOPERMISOS_PERMISOS,GRUPO_DE_PERMISOS, PERMISOS)\
            .join(PERMISOS, GRUPOPERMISOS_PERMISOS.permisos_id == PERMISOS.id)\
            .join(GRUPO_DE_PERMISOS, GRUPOPERMISOS_PERMISOS.grupopermisos_id == GRUPO_DE_PERMISOS.id)\
            .filter(GRUPOPERMISOS_PERMISOS.grupopermisos_id == correo[3].id).all()
        
        # Generar el token y devolver los permisos asociados al grupo
        
        permisos_grupo = {}

        for permiso in grupo_permisos:
            grupo_nombre = permiso[1].nombre
            permiso_nombre = permiso[2].nombre
            if grupo_nombre in permisos_grupo:
                permisos_grupo[grupo_nombre].append({"nombre_permiso":permiso_nombre})
            else:
                permisos_grupo[grupo_nombre] = [{"nombre_permiso":permiso_nombre}]
        token = generate_token({'cliente_id':correo[0].cliente_id,'correo':correo[0].email,"permisos":permisos_grupo,"exp":self.time}) 
        print(permisos_grupo,self.time) 
        return {'token':token,'exp':self.time}, 200
            