from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from services.orders.middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import DIRECCION
from db.connect import get_db
from models.direccion import Direccion
from fastapi import HTTPException



router_api_direc = APIRouter()


@router_api_direc.get("/direccion",response_model=list[Direccion],tags=["direccion"],status_code=status.HTTP_200_OK)
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        direccion = db.query(DIRECCION).all()
        if not direccion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron direcciones")
        response.status_code = status.HTTP_200_OK
        return direccion
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener las direcciones")

@router_api_direc.get("/direccion/{id}", response_model=Direccion, tags=["direccion"],)
@auth_required("view")
async def get_one(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        direccion = db.query(DIRECCION).filter(DIRECCION.id==id).first()
        if not direccion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la direccion")
        response.status_code = status.HTTP_200_OK
        return direccion
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener la direccion")
@router_api_direc.post("/direccion", response_model=Direccion, tags=["direccion"], status_code=status.HTTP_201_CREATED)
@auth_required("insert")
async def create_direccion(request:Request,direccion: Direccion, response: Response, db: Session = Depends(get_db)):
    try:      
        db.add(direccion.dict())
        db.commit()
        db.refresh(direccion.dict())
        response.status_code = status.HTTP_201_CREATED
        return direccion.dict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la direccion")
@router_api_direc.put("/direccion/{id}", response_model=Direccion, tags=["direccion"], status_code=status.HTTP_200_OK)
@auth_required("update")
async def update_direccion(request:Request,id:int, direccion: Direccion, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(DIRECCION).filter(DIRECCION.id==id).update(direccion.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return direccion.dict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar la direccion")
@router_api_direc.delete("/direccion/{id}", response_model=Direccion, tags=["direccion"], status_code=status.HTTP_200_OK)
@auth_required("delete")
async def delete_direccion(request:Request,id:int, response: Response, db: Session = Depends(get_db)):
    try:
        direccion = db.query(DIRECCION).filter(DIRECCION.id==id).first()
        if not direccion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la direccion")
        db.delete(direccion)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return direccion.dict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar la direccion")