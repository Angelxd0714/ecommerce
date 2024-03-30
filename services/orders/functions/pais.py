from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import PAIS
from db.connect import get_db
from models.pais import Pais
from fastapi import HTTPException



router_api_dept = APIRouter()


@router_api_dept.get("/departamentos",response_model=list[Pais],tags=["departamentos"],status_code=status.HTTP_200_OK)
async def get_all(response: Response, db: Session = Depends(get_db)):
    try:
        paises = db.query(PAIS).all()
        if paises is None:
            raise HTTPException(status_code=404, detail="Paises no encontrados")
        response.status_code = status.HTTP_200_OK
        return paises
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los paises")
    
@router_api_dept.get("/departamentos/{id}", response_model=Pais, tags=["departamentos"],status_code=status.HTTP_200_OK)
async def get_one(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        pais = db.query(PAIS).filter(PAIS.id == id).first()
        if pais is None:
            raise HTTPException(status_code=404, detail="Pais no encontrado")
        response.status_code = status.HTTP_200_OK
        return pais
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el pais")
    
@router_api_dept.post("/departamentos", response_model=Pais, tags=["departamentos"],status_code=status.HTTP_201_CREATED)
async def create_pais(pais: Pais, response: Response, db: Session = Depends(get_db)):
    try:
        db.add(pais)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return pais
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el pais")

@router_api_dept.put("/departamentos/{id}", response_model=Pais, tags=["departamentos"], status_code=status.HTTP_200_OK)
async def update_pais(id: int, pais: Pais, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(PAIS).filter(PAIS.id == id).update(pais.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return pais
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el pais")

@router_api_dept.delete("/departamentos/{id}", response_model=Pais, tags=["departamentos"], status_code=status.HTTP_200_OK)
async def delete_pais(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        pais_delete = db.query(PAIS).filter(PAIS.id == id).first()
        if pais_delete is None:
            raise HTTPException(status_code=404, detail="Pais no encontrado")
        db.delete(pais_delete)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return pais_delete
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al borrar el pais")
    