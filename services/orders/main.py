from fastapi import FastAPI, Request
import uvicorn
from functions.municipio import router_api_mun
from functions.categoria import router_api_cat
from functions.direccion import router_api_direc
from functions.ciudades  import router_api_ciu
from functions.departamento import router_api_dept
from functions.pais import router_api_pais
from functions.imagen_producto import router_api_imagen_prod
from functions.producto import router_api_producto
from functions.pedido import router_api_pedido
from functions.det_pedido import router_api_det_pedido
from functions.det_producto import router_api_det_prod

app = FastAPI(debug=True)

app.include_router(router_api_mun)
app.include_router(router_api_cat)
app.include_router(router_api_direc)
app.include_router(router_api_ciu)
app.include_router(router_api_dept)
app.include_router(router_api_pais)
app.include_router(router_api_imagen_prod)
app.include_router(router_api_producto)
app.include_router(router_api_pedido)
app.include_router(router_api_det_pedido)
app.include_router(router_api_det_prod)

#puerto 8000
uvicorn.run(app, host="0.0.0.0", port=8000)