from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import IMAGEN_PRODUCTO
from db.connect import get_db
from models.imagen_producto  import ImagenProducto
from fastapi import HTTPException,UploadFile
import os
import shutil



router_api_imagen_prod = APIRouter()



@router_api_imagen_prod.get("/imagen_producto",response_model=list[ImagenProducto],tags=["imagen_producto"])
@auth_required("view")
async def get_all(request:Request,response:Response,upload:UploadFile,db:Session=Depends(get_db)):
    try:
        imagen_producto = db.query(IMAGEN_PRODUCTO).all()
        if not imagen_producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron imagen_producto")
        response.status_code = status.HTTP_200_OK
        return imagen_producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los productos")
    
@router_api_imagen_prod.get("/imagen_producto/{id}", response_model=ImagenProducto, tags=["imagen_producto"])
@auth_required("view")
async def get_one(request:Request,id:int, response:Response, db:Session=Depends(get_db)):
    try:
        imagen_producto = db.query(IMAGEN_PRODUCTO).filter(IMAGEN_PRODUCTO.id==id).first()
        if not imagen_producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la imagen_producto")
        response.status_code = status.HTTP_200_OK
        return imagen_producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener la imagen_producto")

@router_api_imagen_prod.post("/imagen_producto", response_model=ImagenProducto, tags=["imagen_producto"])
@auth_required("insert")
async def create_imagen_producto(request:Request,upload:UploadFile, response: Response, db: Session = Depends(get_db)):
    file_save = os.mkdirs("uploads/imagen_producto/",exist_ok=True)
    ruta = os.path.join(file_save, upload.filename)
    try:
        with open(ruta, "wb") as buffer:
            shutil.copyfileobj(upload.file, buffer)

        new_imagen_producto = IMAGEN_PRODUCTO(
            url=ruta
        )
        db.add(new_imagen_producto)
        db.commit()
        db.refresh(new_imagen_producto)
        response.status_code = status.HTTP_201_CREATED
        return new_imagen_producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la imagen_producto")
    
@router_api_imagen_prod.put("/imagen_producto/{id}", response_model=ImagenProducto, tags=["imagen_producto"])
@auth_required("update")
async def update_imagen_producto(request:Request,id:int, upload:UploadFile, response: Response, db: Session = Depends(get_db)):
    file_save = os.mkdirs("uploads/imagen_producto/", exist_ok=True)
    ruta = os.path.join(file_save, upload.filename)
    try:
        with open(ruta, "wb") as buffer:
            shutil.copyfileobj(upload.file, buffer)

        db.query(IMAGEN_PRODUCTO).filter(IMAGEN_PRODUCTO.id==id).update(
            {
                "url":ruta
            }
        )
        db.commit()
        imagen_producto = db.query(IMAGEN_PRODUCTO).filter(IMAGEN_PRODUCTO.id==id).first()
        response.status_code = status.HTTP_200_OK
        return imagen_producto
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar la imagen_producto")

@router_api_imagen_prod.delete("/imagen_producto/{id}", response_model=ImagenProducto, tags=["imagen_producto"])
@auth_required("delete")
async def delete_imagen_producto(request:Request,id:int, response: Response, db: Session = Depends(get_db)):
    try:
        imagen_producto = db.query(IMAGEN_PRODUCTO).filter(IMAGEN_PRODUCTO.id==id).first()
        if not imagen_producto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro la imagen_producto")
        db.delete(imagen_producto)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return imagen_producto.dict()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar la imagen_producto")