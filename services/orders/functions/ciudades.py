from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import CIUDADES
from db.connect import get_db
from models.ciudades import Ciudades
from fastapi import HTTPException



router_api_ciu = APIRouter()


@router_api_ciu.get("/ciudades",response_model=list[Ciudades],tags=["ciudades"],status_code=status.HTTP_200_OK)
async def get_all(response: Response, db: Session = Depends(get_db)):
    try:
        ciudades = db.query(CIUDADES).all()
        if ciudades is None:
            raise HTTPException(status_code=404, detail="Ciudades no encontradas")
        response.status_code = status.HTTP_200_OK
        return ciudades
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")
    
@router_api_ciu.get("/ciudades/{id}", response_model=Ciudades, tags=["ciudades"],status_code=status.HTTP_200_OK)
async def get_one(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        ciudad = db.query(CIUDADES).filter(CIUDADES.id == id).first()
        if ciudad is None:
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
        response.status_code = status.HTTP_200_OK
        return ciudad
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")

@router_api_ciu.post("/ciudades", response_model=Ciudades, tags=["ciudades"],status_code=status.HTTP_200_OK)
async def create_ciudad(ciudad:Ciudades,response:Response, db:Session=Depends(get_db)):
    try:
        db.add(ciudad)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return ciudad
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor: {e}")


@router_api_ciu.put("/ciudades/{id}", response_model=Ciudades, tags=["ciudades"],status_code=200)
async def update_ciudad(id:int, ciudad:Ciudades,response:Response, db:Session=Depends(get_db)):
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
async def delete_ciudad(id:int,response:Response ,db:Session=Depends(get_db)):
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