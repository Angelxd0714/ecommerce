from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import CIUDADES
from db.connect import get_db
from models.ciudades import Ciudades
from fastapi import HTTPException
from middleware.authentication import auth_required


router_api_ciu = APIRouter()


@router_api_ciu.get("/ciudades",response_model=list[Ciudades],tags=["ciudades"],status_code=status.HTTP_200_OK)
@auth_required("view")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_all(request:Request,response: Response, db: Session = Depends(get_db)):
    try:
        ciudades = db.query(CIUDADES).all()
        if ciudades is None:
            raise HTTPException(status_code=404, detail="Ciudades no encontradas")
        response.status_code = status.HTTP_200_OK
        return ciudades
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")
    
@router_api_ciu.get("/ciudades/{id}", response_model=Ciudades, tags=["ciudades"],status_code=status.HTTP_200_OK)
@auth_required("view")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_one(id: int,request:Request, response: Response, db: Session = Depends(get_db)):
    try:
        ciudad = db.query(CIUDADES).filter(CIUDADES.id == id).first()
        if ciudad is None:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        response.status_code = status.HTTP_200_OK
        return ciudad
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")

@router_api_ciu.post("/ciudades", response_model=Ciudades, tags=["ciudades"],status_code=status.HTTP_200_OK)
@auth_required("insert")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def create_ciudad(request:Request,ciudad:Ciudades,response:Response, db:Session=Depends(get_db)):
    try:
        db.add(ciudad)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return ciudad
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")


@router_api_ciu.put("/ciudades/{id}", response_model=Ciudades, tags=["ciudades"],status_code=200)
@auth_required("update")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def update_ciudad(request:Request,id:int, ciudad:Ciudades,response:Response, db:Session=Depends(get_db)):
    try:
        ciudad_update = db.query(CIUDADES).filter(CIUDADES.id==id).first()
        if ciudad_update is None:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        ciudad_update.nombre = ciudad.nombre
        db.commit()
        response.status_code = status.HTTP_200_OK
        return ciudad_update
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    
@router_api_ciu.delete("/ciudades/{id}", response_model=Ciudades, tags=["ciudades"],status_code=200)
@auth_required("delete")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def delete_ciudad(request:Request,id:int,response:Response ,db:Session=Depends(get_db)):
    try:
        ciudad_delete = db.query(CIUDADES).filter(CIUDADES.id==id).first()
        if ciudad_delete is None:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        db.delete(ciudad_delete)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return ciudad_delete
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)