from fastapi import FastAPI
from functions.facturas import router_api_factura
from functions.estado_pago import router_api_estado_pago
from functions.paypal import router_api_paypal
from functions.tarjetas import router_api_tarjetas
app = FastAPI(debug=True)

app.include_router(router_api_factura)
app.include_router(router_api_estado_pago)
app.include_router(router_api_paypal)
app.include_router(router_api_tarjetas)


#puerto 6500