from fastapi import APIRouter, Depends, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import PRODUCTOS
from db.connect import get_db
from models.producto import Producto
from fastapi import HTTPException



router_api_producto = APIRouter()



@router_api_producto.get("/productos",response_model=list[Producto],tags=["productos"])
async def get_all(response:Response,db:Session=Depends(get_db)):
    try:
        productos = db.query(PRODUCTOS).all()
        if not productos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron productos")
        response.status_code = status.HTTP_200_OK
        return productos
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los productos")

@router_api_producto.get("/productos/{id}", response_model=Producto, tags=["productos"])
async def get_one(id:int, response:Response, db:Session=Depends(get_db)):
    try:
        producto = db.query(PRODUCTOS).filter(PRODUCTOS.id == id).first()
        if not producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el producto")
        response.status_code = status.HTTP_200_OK
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el producto")

@router_api_producto.post("/productos", response_model=Producto, tags=["productos"])
async def create_producto(producto: Producto, response: Response, db: Session = Depends(get_db)):
    try:
        db.add(producto)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el producto")

@router_api_producto.put("/productos/{id}", response_model=Producto, tags=["productos"])
async def update_producto(id: int, producto: Producto, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(PRODUCTOS).filter(PRODUCTOS.id==id).update(producto.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el producto")

@router_api_producto.delete("/productos/{id}", response_model=Producto, tags=["productos"])
async def delete_producto(id: int, response: Response, db: Session = Depends(get_db)):
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
