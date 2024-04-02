from fastapi import APIRouter, Depends, HTTPException,status,Response

from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import ESTADO_PAGO
from db.connect import get_db
from models.estado_pago import Estado_Pago



router_api_estado_pago = APIRouter()

@router_api_estado_pago.get("/estado_pago",response_model=list[Estado_Pago],tags=["estado_pago"],status_code=status.HTTP_200_OK)
async def get_all(response:Response,db:Session=Depends(get_db)):
    try:
        estado_pago = db.query(ESTADO_PAGO).all()
        response.status_code = status.HTTP_200_OK
        return estado_pago
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_estado_pago.get("/estado_pago/{id}",response_model=Estado_Pago,tags=["estado_pago"],status_code=status.HTTP_200_OK)
async def get_one(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        estado_pago = db.query(ESTADO_PAGO).filter(ESTADO_PAGO.id == id).first()
        if not estado_pago:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el estado de pago")
        response.status_code = status.HTTP_200_OK
        return estado_pago
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_estado_pago.post("/estado_pago",response_model=Estado_Pago,tags=["estado_pago"],status_code=status.HTTP_201_CREATED)
async def create_estado_pago(estado_pago: Estado_Pago,response:Response,db:Session=Depends(get_db)):
    try:
        db.add(estado_pago)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return estado_pago
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_estado_pago.put("/estado_pago/{id}",response_model=Estado_Pago,tags=["estado_pago"],status_code=status.HTTP_200_OK)
async def update_estado_pago(id:int, estado_pago: Estado_Pago, response:Response, db:Session=Depends(get_db)):
    try:
        db.query(ESTADO_PAGO).filter(ESTADO_PAGO.id == id).update(estado_pago.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return estado_pago
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_estado_pago.delete("/estado_pago/{id}", response_model=Estado_Pago, tags=["estado_pago"])
async def delete_estado_pago(id: int, response: Response, db: Session = Depends(get_db)):
        try:
            estado_pago = db.query(ESTADO_PAGO).filter(ESTADO_PAGO.id == id).first()
            if not estado_pago:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el estado de pago")
            db.delete(estado_pago)
            db.commit()
            response.status_code = status.HTTP_200_OK
            return estado_pago
        except:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")