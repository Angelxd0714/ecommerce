from typing import List
from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from middleware.authentication import auth_required
from config.models import CATEGORIA
from db.connect import get_db
from models.categoria import Categoria
from fastapi import HTTPException



router_api_cat = APIRouter()


@router_api_cat.get("/categoria",response_model=List[Categoria],tags=["categoria"],status_code=status.HTTP_200_OK)  # Ruta protegida por el middleware de autenticación. Solo los usuarios con rol "admin" pueden acceder a esta ruta.     # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        categoria = db.query(CATEGORIA).order_by(CATEGORIA.id).all()
        if categoria is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la categoria")
        response.status_code = status.HTTP_200_OK
        return categoria
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_cat.get("/categoria/{id}",response_model=Categoria,tags=["categoria"],status_code=status.HTTP_200_OK)
 # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_one(id:int,request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        categoria = db.query(CATEGORIA).filter(CATEGORIA.id == id).first()
        if not categoria:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la categoria")
        response.status_code = status.HTTP_200_OK
        return categoria
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_cat.post("/categoria",response_model=Categoria,tags=["categoria"],status_code=status.HTTP_201_CREATED)
async def create_categoria(request:Request,categoria: Categoria,response:Response,db:Session=Depends(get_db)):
    try:
        categoria_db = CATEGORIA(nombre=categoria.nombre)  # Crea una instancia del modelo de Categoría
        db.add(categoria_db)
        db.commit()
        db.refresh(categoria_db)
        response.status_code = status.HTTP_201_CREATED
        return categoria_db  # Devuelve la instancia del modelo creada
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}')

@router_api_cat.put("/categoria/{id}",response_model=Categoria,tags=["categoria"],status_code=status.HTTP_200_OK)

async def update_categoria(request: Request, id: int, categoria: Categoria, response: Response, db: Session = Depends(get_db)):
    try:
        # Filtrar la categoría que se desea actualizar
        categoria_db = db.query(CATEGORIA).filter(CATEGORIA.id == id).first()
        if categoria_db:
            # Actualizar los campos de la categoría con los valores proporcionados
            db.query(CATEGORIA).filter(CATEGORIA.id == id).update(categoria.dict())
            db.commit()
            # Actualizar el objeto de categoría con los nuevos valores
            categoria_db = db.query(CATEGORIA).filter(CATEGORIA.id == id).first()
            response.status_code = status.HTTP_200_OK
            return categoria_db
        else:
            # La categoría con el ID especificado no fue encontrada
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    except Exception as e:
        # Manejar cualquier error interno del servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router_api_cat.delete("/categoria/{id}",response_model=Categoria,tags=["categoria"],status_code=status.HTTP_200_OK)

async def delete_categoria(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        categoria = db.query(CATEGORIA).filter(CATEGORIA.id == id).first()
        if not categoria:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la categoria")
        db.delete(categoria)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return categoria
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
