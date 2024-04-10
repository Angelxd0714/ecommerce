from fastapi import APIRouter, Depends, HTTPException, Request,status,Response

from sqlalchemy.orm import Session
import sys

from middleware.authentication import auth_required
sys.path.append('/home/angel/Documents/ecommerce/')
from config.models import PAYPAL
from db.connect import get_db
from models.paypal import Paypal

router_api_paypal = APIRouter()

@router_api_paypal.get("/paypal",response_model=list[Paypal],tags=["paypal"])
@auth_required("view")
async def get_all(request:Request,response:Response,db:Session=Depends(get_db)):
    try:
        paypal = db.query(PAYPAL).all()
        if paypal is None:
            raise HTTPException(status_code=404, detail="Paypal no encontrados")
        response.status_code = status.HTTP_200_OK
        return paypal
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_paypal.get("/paypal/{id}",response_model=Paypal,tags=["paypal"])
@auth_required("view")
async def get_one(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        paypal = db.query(PAYPAL).filter(PAYPAL.id == id).first()
        if paypal is None:
            raise HTTPException(status_code=404, detail="Paypal no encontrado")
        response.status_code = status.HTTP_200_OK
        return paypal
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_paypal.post("/paypal",response_model=Paypal,tags=["paypal"])
@auth_required("insert")
async def create_paypal(request:Request,paypal: Paypal,response:Response,db:Session=Depends(get_db)):
    try:
        db.add(paypal)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return paypal
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
@router_api_paypal.put("/paypal/{id}",response_model=Paypal,tags=["paypal"])
@auth_required("update")
async def update_paypal(request:Request,id:int, paypal: Paypal, response:Response, db:Session=Depends(get_db)):
    try:
        db.query(PAYPAL).filter(PAYPAL.id == id).update(paypal.model_dump())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return paypal
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

@router_api_paypal.delete("/paypal/{id}", response_model=Paypal, tags=["paypal"])
@auth_required("delete")
async def delete_paypal(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        paypal = db.query(PAYPAL).filter(PAYPAL.id == id).first()
        if not paypal:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paypal no encontrado")
        db.delete(paypal)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return paypal
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")