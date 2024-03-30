from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import DIRECCION
from db.connect import get_db
from models.direccion import Direccion
from fastapi import HTTPException



router_api_direc = APIRouter()


@router_api_direc.get("/direccion",response_model=list[Direccion],tags=["direccion"],status_code=status.HTTP_200_OK)
async def get_all(response:Response,db:Session=Depends(get_db)):
    direccion = db.query(DIRECCION).all()
    if not direccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron direcciones")
    response.status_code = status.HTTP_200_OK
    return direccion

@router_api_direc.get("/direccion/{id}", response_model=Direccion, tags=["direccion"],)
async def get_one(id:int, response:Response, db:Session=Depends(get_db)):
    direccion = db.query(DIRECCION).filter(DIRECCION.id==id).first()
    if not direccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la direccion")
    response.status_code = status.HTTP_200_OK
    return direccion

