import os
from dotenv import load_dotenv
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
import jwt
import sys
from datetime import datetime, timedelta
sys.path.append('/home/angel/Documents/ecommerce/')
try:
    load_dotenv("/home/angel/Documents/ecommerce/config/.env")
except Exception as e:
    print(e)

def auth_required(permission):
    def decorator(f):
        async def decorated(*args, **kwargs):
            request = args[0]  # Se espera que el primer argumento sea la solicitud en FastAPI
            token = request.headers.get('Authorization')

            if not token:
                return JSONResponse(content={'message': 'Token no encontrado'}, status_code=401)
            
            if not token.startswith('Bearer '):
                return JSONResponse(content={'message': 'Token inválido'}, status_code=401)
            
            encoded_token = token.split(maxsplit=1)[1]

            try:
                decode = jwt.decode(encoded_token, os.environ.get("SECRET_KEY"), algorithms=['HS256'])
                user = decode
                
                # Obtén los permisos del usuario desde el token
                permisos_usuario = user.get("permisos", {}).get("grupo_permisos_administradores", [])
                
                # Verifica si el usuario tiene el permiso requerido
                tiene_permiso = False
                for permiso in permisos_usuario:
                    if permiso.get("nombre_permiso") == permission:
                        tiene_permiso = True
                        break
                
                if not tiene_permiso:
                    return JSONResponse(content={'message': 'Acceso denegado'}, status_code=403)
                
                return await f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return JSONResponse(content={'message': 'Token expirado'}, status_code=401)
            except jwt.InvalidTokenError as e:
                return JSONResponse(content={'message': f'{e}'}, status_code=401)
        return decorated
    return decorator



