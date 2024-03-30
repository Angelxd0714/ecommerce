from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import MUNICIPIOS
from db.connect import get_db
from models.municipios import Municipio
from fastapi import HTTPException



router_api_mun = APIRouter()





@router_api_mun.get("/municipios",response_model=list[Municipio],tags=["municipios"])
async def get_all(response:Response,db:Session=Depends(get_db)):
    try:
        municipios = db.query(MUNICIPIOS).all()
        if municipios is None:
            raise HTTPException(status_code=404, detail="Municipios no encontrados")
        response.status_code = status.HTTP_200_OK
        return municipios
    except Exception as e:
        return e
    
@router_api_mun.get("/municipios/{id}", response_model=Municipio, tags=["municipios"])
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
async def create_municipio(municipio:Municipio,response:Response, db:Session=Depends(get_db)):
        try:
            db.add(municipio)
            db.commit()
            response.status_code = status.HTTP_200_OK
            return municipio
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)

@router_api_mun.put("/municipios/{id}", response_model=Municipio, tags=["municipios"],status_code=200)
async def update_municipio(id:int, municipio:Municipio,response:Response, db:Session=Depends(get_db)):
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
async def delete_municipio(id:int,response:Response ,db:Session=Depends(get_db)):
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