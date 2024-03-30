from fastapi import FastAPI
from functions.municipio import router_api_mun

app = FastAPI(debug=True)

app.include_router(router_api_mun)

