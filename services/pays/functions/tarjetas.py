from fastapi import APIRouter, Depends, HTTPException, Request,status,Response

from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import TARJETAS
from db.connect import get_db
from models.tarjetas import Tarjetas



router_api_tarjetas = APIRouter()

@router_api_tarjetas.get("/tarjetas",response_model=list[Tarjetas],tags=["tarjetas"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        tarjetas = db.query(TARJETAS).all()
        response.status_code = status.HTTP_200_OK
        return tarjetas
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
@router_api_tarjetas.get("/tarjetas/{id}",response_model=Tarjetas,tags=["tarjetas"])
@auth_required("view")
async def get_one(request:Request,id:int,response:Response,db:Session=Depends(get_db)):
    try:
        tarjeta = db.query(TARJETAS).filter(TARJETAS.id == id).first()
        if not tarjeta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la tarjeta")
        response.status_code = status.HTTP_200_OK
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
@router_api_tarjetas.post("/tarjetas",response_model=Tarjetas,tags=["tarjetas"],status_code=status.HTTP_201_CREATED)
@auth_required("insert")
async def create_tarjeta(request:Request,tarjeta: Tarjetas,response:Response,db:Session=Depends(get_db)):
    try:
        db.add(tarjeta)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_tarjetas.put("/tarjetas/{id}",response_model=Tarjetas,tags=["tarjetas"],status_code=status.HTTP_200_OK)
@auth_required("update")
async def update_tarjeta(request:Request,id:int, tarjeta: Tarjetas, response:Response, db:Session=Depends(get_db)):
    try:
        db.query(TARJETAS).filter(TARJETAS.id == id).update(tarjeta.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return tarjeta
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_tarjetas.delete("/tarjetas/{id}", response_model=Tarjetas, tags=["tarjetas"])
@auth_required("delete")
async def delete_tarjeta(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        tarjeta = db.query(TARJETAS).filter(TARJETAS.id == id).first()
        if not tarjeta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la tarjeta")
        db.delete(tarjeta)
        db.commit()
        response.status_code = status.HTTP_200_OK
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")