from functools import wraps
import os
from typing import Callable
from dotenv import load_dotenv
from fastapi import Body, Header, Request, HTTPException, status
from fastapi.responses import JSONResponse
import jwt
import sys
from datetime import datetime, timedelta
from pydantic import BaseModel
from requests import request

from models.permisos import Permisos
sys.path.append('/home/angel/Documents/ecommerce/')
try:
    load_dotenv("/home/angel/Documents/ecommerce/config/.env")
except Exception as e:
    print(e)
def auth_required(permission: str):
    def decorator(func):
        @wraps(func)
        async def decorated(request: Request, *args, **kwargs):
            # Decodificar token
            token = request.headers.get('Authorization')
            if not token or not token.startswith('Bearer '):
                raise HTTPException(status_code=401, detail='Token no encontrado')
            encoded_token = token.split(' ')[1]

            # Obtener permisos del token
            try:
                decode = jwt.decode(encoded_token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
                user_permisos = decode.get("permisos", {}).get("grupo_permisos_administradores")
                print(user_permisos)
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail='Token expirado')
            except jwt.InvalidTokenError as e:
                raise HTTPException(status_code=401, detail=f'Token inválido: {e}')

            # Verificar permisos
            if not any(permiso["nombre_permiso"] == permission for permiso in user_permisos):
                raise HTTPException(status_code=403, detail='Acceso denegado')

            # Ejecutar la función original
            return await func(request, *args, **kwargs)
        return decorated
    return decorator