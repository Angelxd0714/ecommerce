from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import PEDIDO
from db.connect import get_db
from models.pedido import Pedido
from fastapi import HTTPException



router_api_pedido = APIRouter()

@router_api_pedido.get("/pedido",response_model=list[Pedido],tags=["pedido"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        pedido = db.query(PEDIDO).all()
        response.status_code = status.HTTP_200_OK
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los pedidos")

@router_api_pedido.get("/pedido/{id}", response_model=Pedido, tags=["pedido"])
@auth_required("view")
async def get_one(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        pedido = db.query(PEDIDO).filter(PEDIDO.id == id).first()
        if not pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el pedido")
        response.status_code = status.HTTP_200_OK
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el pedido")

@router_api_pedido.post("/pedido", response_model=Pedido, tags=["pedido"])
@auth_required("insert")
async def create_pedido(request:Request,pedido: Pedido, response: Response, db: Session = Depends(get_db)):
    try:
        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        response.status_code = status.HTTP_201_CREATED
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el pedido")

@router_api_pedido.put("/pedido/{id}", response_model=Pedido, tags=["pedido"])
@auth_required("update")
async def update_pedido(request:Request,id:int, pedido: Pedido, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(PEDIDO).filter(PEDIDO.id == id).update(pedido.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el pedido")

@router_api_pedido.delete("/pedido/{id}", response_model=Pedido, tags=["pedido"])
@auth_required("delete")
async def delete_pedido(request:Request,id:int, response: Response, db: Session = Depends(get_db)):
    try:
        pedido = db.query(PEDIDO).filter(PEDIDO.id == id).first()
        if not pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el pedido")
        db.delete(pedido)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el pedido")
    