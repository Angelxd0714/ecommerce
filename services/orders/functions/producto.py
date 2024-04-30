from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from services.orders.middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import PRODUCTOS
from db.connect import get_db
from models.producto import Producto
from fastapi import HTTPException



router_api_producto = APIRouter()



@router_api_producto.get("/productos",response_model=list[Producto],tags=["productos"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        productos = db.query(PRODUCTOS).all()
        if not productos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron productos")
        response.status_code = status.HTTP_200_OK
        return productos
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los productos")

@router_api_producto.get("/productos/{id}", response_model=Producto, tags=["productos"])
@auth_required("view")
async def get_one(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        producto = db.query(PRODUCTOS).filter(PRODUCTOS.id == id).first()
        if not producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el producto")
        response.status_code = status.HTTP_200_OK
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el producto")

@router_api_producto.post("/productos", response_model=Producto, tags=["productos"])
@auth_required("insert")
async def create_producto(request:Request,producto: Producto, response: Response, db: Session = Depends(get_db)):
    try:
        categoria = PRODUCTOS(**producto.dict())
        db.add(categoria)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return {'success': 200, 'message': 'Producto created successfully'}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el producto")

@router_api_producto.put("/productos/{id}", response_model=Producto, tags=["productos"])
@auth_required("update")
async def update_producto(request:Request,id: int, producto: Producto, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(PRODUCTOS).filter(PRODUCTOS.id==id).update(producto.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el producto")

@router_api_producto.delete("/productos/{id}", response_model=Producto, tags=["productos"])
@auth_required("delete")
async def delete_producto(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        producto = db.query(PRODUCTOS).filter(PRODUCTOS.id==id).first()
        if not producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el producto")
        db.delete(producto)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al borrar el producto")


