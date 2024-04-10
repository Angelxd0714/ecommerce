from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import MUNICIPIOS
from db.connect import get_db
from models.municipios import Municipio
from fastapi import HTTPException



router_api_mun = APIRouter()





@router_api_mun.get("/municipios",response_model=list[Municipio],tags=["municipios"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        municipios = db.query(MUNICIPIOS).all()
        if municipios is None:
            raise HTTPException(status_code=404, detail="Municipios no encontrados")
        response.status_code = status.HTTP_200_OK
        return municipios
    except Exception as e:
        return e
    
@router_api_mun.get("/municipios/{id}", response_model=Municipio, tags=["municipios"])
@auth_required("view")
async def get_one(id:int,response:Response ,db:Session=Depends(get_db)):
    try:
        municipio = db.query(MUNICIPIOS).filter(MUNICIPIOS.id==id).first()
        if municipio is None:
            raise HTTPException(status_code=404, detail="Municipio no encontrado")
        response.status_code = status.HTTP_200_OK
        return municipio
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

@router_api_mun.post("/municipios", response_model=Municipio, tags=["municipios"],status_code=200)
@auth_required("insert")
async def create_municipio(request:Request,municipio:Municipio,response:Response, db:Session=Depends(get_db)):
        try:
            db.add(municipio)
            db.commit()
            response.status_code = status.HTTP_200_OK
            return municipio
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)

@router_api_mun.put("/municipios/{id}", response_model=Municipio, tags=["municipios"],status_code=200)
@auth_required("update")
async def update_municipio(request:Request,id:int, municipio:Municipio,response:Response, db:Session=Depends(get_db)):
    try:
        municipio_update = db.query(MUNICIPIOS).filter(MUNICIPIOS.id==id).first()
        if municipio_update is None:
            raise HTTPException(status_code=404, detail="Municipio no encontrado")
        municipio_update.nombre = municipio.nombre
        db.commit()
        response.status_code = status.HTTP_200_OK
        return municipio_update
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
@router_api_mun.delete("/municipios/{id}", response_model=Municipio, tags=["municipios"],status_code=200)
@auth_required("delete")
async def delete_municipio(request:Request,id:int,response:Response ,db:Session=Depends(get_db)):
    try:
        municipio_delete = db.query(MUNICIPIOS).filter(MUNICIPIOS.id==id).first()
        if municipio_delete is None:
            raise HTTPException(status_code=404, detail="Municipio no encontrado")
        db.delete(municipio_delete)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return municipio_delete
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)