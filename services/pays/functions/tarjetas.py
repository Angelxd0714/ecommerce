from fastapi import APIRouter, Depends, HTTPException,status,Response

from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import TARJETAS
from db.connect import get_db
from models.tarjetas import Tarjetas



router_api_tarjetas = APIRouter()

@router_api_tarjetas.get("/tarjetas",response_model=list[Tarjetas],tags=["tarjetas"])
async def get_all(response:Response,db:Session=Depends(get_db)):
    try:
        tarjetas = db.query(TARJETAS).all()
        response.status_code = status.HTTP_200_OK
        return tarjetas
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
@router_api_tarjetas.get("/tarjetas/{id}",response_model=Tarjetas,tags=["tarjetas"])
async def get_one(id:int,response:Response,db:Session=Depends(get_db)):
    try:
        tarjeta = db.query(TARJETAS).filter(TARJETAS.id == id).first()
        if not tarjeta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la tarjeta")
        response.status_code = status.HTTP_200_OK
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
@router_api_tarjetas.post("/tarjetas",response_model=Tarjetas,tags=["tarjetas"],status_code=status.HTTP_201_CREATED)
async def create_tarjeta(tarjeta: Tarjetas,response:Response,db:Session=Depends(get_db)):
    try:
        db.add(tarjeta)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_tarjetas.put("/tarjetas/{id}",response_model=Tarjetas,tags=["tarjetas"],status_code=status.HTTP_200_OK)
async def update_tarjeta(id:int, tarjeta: Tarjetas, response:Response, db:Session=Depends(get_db)):
    try:
        db.query(TARJETAS).filter(TARJETAS.id == id).update(tarjeta.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_tarjetas.delete("/tarjetas/{id}", response_model=Tarjetas, tags=["tarjetas"])
async def delete_tarjeta(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        tarjeta = db.query(TARJETAS).filter(TARJETAS.id == id).first()
        if not tarjeta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la tarjeta")
        db.delete(tarjeta)
        db.commit()
        response.status_code = status.HTTP_200_OK
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")