from fastapi import APIRouter, Depends, Request, Response,status
from sqlalchemy.orm import Session
import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from middleware.authentication import auth_required
from config.models import DEPARTAMENTOS
from db.connect import get_db
from models.departamentos import Departamentos
from fastapi import HTTPException



router_api_dept = APIRouter()


@router_api_dept.get("/departamentos",response_model=list[Departamentos],tags=["departamentos"],status_code=status.HTTP_200_OK)
@auth_required("view")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_all(request:Request,response: Response, db: Session = Depends(get_db)):
    try:
        departamentos = db.query(DEPARTAMENTOS).all()
        if departamentos is None:
            raise HTTPException(status_code=404, detail="Departamentos no encontrados")
        response.status_code = status.HTTP_200_OK
        return departamentos
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los departamentos")

@router_api_dept.get("/departamentos/{id}", response_model=Departamentos, tags=["departamentos"],status_code=status.HTTP_200_OK)
@auth_required("view")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def get_one(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        departamento = db.query(DEPARTAMENTOS).filter(DEPARTAMENTOS.id == id).first()
        if departamento is None:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        response.status_code = status.HTTP_200_OK
        return departamento
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el departamento")

@router_api_dept.post("/departamentos", response_model=Departamentos, tags=["departamentos"],status_code=status.HTTP_201_CREATED)
@auth_required("insert")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def create_departamento(request:Request,departamento: Departamentos, response: Response, db: Session = Depends(get_db)):
    try:
        db.add(departamento)
        db.commit()
        response.status_code = status.HTTP_201_CREATED
        return departamento
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el departamento")

@router_api_dept.put("/departamentos/{id}", response_model=Departamentos, tags=["departamentos"],status_code=status.HTTP_200_OK)
@auth_required("update")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def update_departamento(request:Request,id: int, departamento: Departamentos, response: Response, db: Session = Depends(get_db)):
    try:
        db.query(DEPARTAMENTOS).filter(DEPARTAMENTOS.id == id).update(departamento.dict())
        db.commit()
        response.status_code = status.HTTP_200_OK
        return departamento
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el departamento")

@router_api_dept.delete("/departamentos/{id}", response_model=Departamentos, tags=["departamentos"], status_code=status.HTTP_200_OK)
@auth_required("delete")  # El decorador auth_required() recibe el nombre del rol que debe tener el usuario para acceder a la ruta.
async def delete_departamento(request:Request,id: int, response: Response, db: Session = Depends(get_db)):
    try:
        departamento_delete = db.query(DEPARTAMENTOS).filter(DEPARTAMENTOS.id == id).first()
        if departamento_delete is None:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        db.delete(departamento_delete)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return departamento_delete
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al borrar el departamento")