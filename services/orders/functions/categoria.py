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


@router_api_cat.get("/categoria",response_model=list[Categoria],tags=["categoria"],status_code=status.HTTP_200_OK)  # Ruta protegida por el middleware de autenticación. Solo los usuarios con rol "admin" pueden acceder a esta ruta.     # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        categoria = db.query(CATEGORIA).all()
        if categoria is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la categoria")
        response.status_code = status.HTTP_200_OK
        return {'categoria':categoria}
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
        db.add(categoria)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return categoria
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_cat.put("/categoria/{id}",response_model=Categoria,tags=["categoria"],status_code=status.HTTP_200_OK)

async def update_categoria(request:Request,id:int, categoria: Categoria, response:Response, db:Session=Depends(get_db)):
    try:
        db.query(CATEGORIA).filter(CATEGORIA.id == id).update(categoria.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return categoria
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

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
