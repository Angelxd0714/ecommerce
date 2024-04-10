from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import DET_PEDIDO
from db.connect import get_db
from models.det_pedido import DetPedido
from fastapi import HTTPException



router_api_det_pedido = APIRouter()

@router_api_det_pedido.get("/det_pedido",response_model=list[DetPedido],tags=["det_pedido"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        det_pedido = db.query(DET_PEDIDO).all()
        response.status_code = status.HTTP_200_OK
        return det_pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los detalle_pedido")

@router_api_det_pedido.get("/det_pedido/{id}", response_model=DetPedido, tags=["det_pedido"])
@auth_required("view")
async def get_one(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        det_pedido = db.query(DET_PEDIDO).filter(DET_PEDIDO.id == id).first()
        if not det_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el detalle_pedido")
        response.status_code = status.HTTP_200_OK
        return det_pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el detalle_pedido")

@router_api_det_pedido.post("/det_pedido", response_model=DetPedido, tags=["det_pedido"])
@auth_required("insert")
async def create_det_pedido(request:Request,det_pedido: DetPedido, response: Response, db: Session = Depends(get_db)):
    try:
        db.add(det_pedido)
        db.commit()
        db.refresh(det_pedido)
        response.status_code = status.HTTP_201_CREATED
        return det_pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el detalle_pedido")

@router_api_det_pedido.put("/det_pedido/{id}", response_model=DetPedido, tags=["det_pedido"])
@auth_required("update")
async def update_det_pedido(request:Request,id:int, det_pedido: DetPedido, response: Response, db: Session = Depends(get_db)):
    try:
        det_pedido=db.query(DET_PEDIDO).filter(DET_PEDIDO.id == id).update(det_pedido.dict())
        if not det_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el detalle_pedido")
        db.commit()
        det_pedido = db.query(DET_PEDIDO).filter(DET_PEDIDO.id == id).first()
        response.status_code = status.HTTP_200_OK
        return det_pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el detalle_pedido")

@router_api_det_pedido.delete("/det_pedido/{id}", response_model=DetPedido, tags=["det_pedido"])
@auth_required("delete")
async def delete_det_pedido(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        det_pedido = db.query(DET_PEDIDO).filter(DET_PEDIDO.id == id).first()
        if not det_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el detalle_pedido")
        db.delete(det_pedido)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return det_pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el detalle_pedido")

