from fastapi import APIRouter, Depends, HTTPException,status,Response

from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import FACTURA
from db.connect import get_db
from models.facturas import Facturas

router_api_factura = APIRouter()

@router_api_factura.get("/factura",response_model=list[Facturas],tags=["factura"])
async def get_all(response:Response,db:Session=Depends(get_db)):
    try:
        factura = db.query(FACTURA).all()
        response.status_code = status.HTTP_200_OK
        return factura
    except:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    
@router_api_factura.get("/factura/{id}", response_model=Facturas, tags=["factura"])
async def get_one(id:int, response:Response, db:Session=Depends(get_db)):
    try:
        factura = db.query(FACTURA).filter(FACTURA.id == id).first()
        response.status_code = status.HTTP_200_OK
        return factura
    except:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    
@router_api_factura.post("/factura",response_model=Facturas,tags=["factura"])
async def create_factura(factura: Facturas,response:Response,db:Session=Depends(get_db)):
    try:
        db.add(factura)
        db.commit()
        db.refresh(factura)
        response.status_code = status.HTTP_201_CREATED
        return factura
    except:
        raise HTTPException(status_code=404, detail="Factura no creada")
    


@router_api_factura.put("/factura/{id}",response_model=Facturas,tags=["factura"])
async def update_factura(id:int, factura: Facturas,response:Response,db:Session=Depends(get_db)):
    try:
        factura_update = db.query(FACTURA).filter(FACTURA.id == id).update(factura.dict(),synchronize_session=False)
        if not factura_update:
            raise HTTPException(status_code=404, detail="Factura no encontrada")
        db.commit()
        response.status_code = status.HTTP_200_OK
        return factura_update
    except:
        raise HTTPException(status_code=404, detail="Factura no actualizada")
    

@router_api_factura.delete("/factura/{id}", response_model=Facturas, tags=["factura"])
async def delete_factura(id: int, response: Response, db: Session = Depends(get_db)):
    try:
        factura = db.query(FACTURA).filter(FACTURA.id == id).first()
        if not factura:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Factura no encontrada")
        db.delete(factura)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return factura.dict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar la factura")
    



