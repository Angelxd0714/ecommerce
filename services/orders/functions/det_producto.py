from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import DETALLE_PRODUCTO
from db.connect import get_db
from models.ProductoDet import DetProducto
from fastapi import HTTPException



router_api_det_prod= APIRouter()


@router_api_det_prod.get("/detalle_producto",response_model=list[DetProducto],tags=["detalle_producto"],status_code=status.HTTP_200_OK)
async def get_all(response:Response,db:Session=Depends(get_db)):
 try:
  detalle_producto = db.query(DETALLE_PRODUCTO).all()
  if not detalle_producto:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron detalle_producto")
  response.status_code = status.HTTP_200_OK
  return detalle_producto
 except:
  raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener las detalle_producto")
 
@router_api_det_prod.get("/detalle_producto/{id}", response_model=DetProducto, tags=["detalle_producto"],)
async def get_one(id:int, response:Response, db:Session=Depends(get_db)):
    try:
        detalle_producto = db.query(DETALLE_PRODUCTO).filter(DETALLE_PRODUCTO.id==id).first()
        if not detalle_producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el detalle_producto")
        response.status_code = status.HTTP_200_OK
        return detalle_producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el detalle_producto")
    
@router_api_det_prod.post("/detalle_producto", response_model=DetProducto, tags=["detalle_producto"], status_code=status.HTTP_201_CREATED)
async def create_detalle_producto(detalle_producto: DetProducto, response: Response, db: Session = Depends(get_db)):
   try:
       db.add(detalle_producto)
       db.commit()
       response.status_code = status.HTTP_201_CREATED
       return detalle_producto
   #return {"message": "detalle_producto creado exitosamente"}
   except:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el detalle_producto")
   
@router_api_det_prod.put("/detalle_producto/{id}", response_model=DetProducto, tags=["detalle_producto"], status_code=status.HTTP_200_OK)
async def update_detalle_producto(id:int, detalle_producto: DetProducto, response: Response, db: Session = Depends(get_db)):
   try:
       db.query(DETALLE_PRODUCTO).filter(DETALLE_PRODUCTO.id==id).update(detalle_producto.dict())
       db.commit()
       response.status_code = status.HTTP_200_OK
       return detalle_producto
   except:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el detalle_producto")
   
@router_api_det_prod.delete("/detalle_producto/{id}", response_model=DetProducto, tags=["detalle_producto"], status_code=status.HTTP_200_OK)
async def delete_detalle_producto(id:int, response: Response, db: Session = Depends(get_db)):
   try:
       detalle_producto = db.query(DETALLE_PRODUCTO).filter(DETALLE_PRODUCTO.id==id).first()
       if not detalle_producto:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el detalle_producto")
       db.delete(detalle_producto)
       db.commit()
       response.status_code = status.HTTP_200_OK
       return detalle_producto
   except:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el detalle_producto")