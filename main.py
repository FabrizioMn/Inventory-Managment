import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.transacciones import router as transacciones_router
from src.routes.productos import router as productos_router
from src.routes.proveedores import router as proveedores_router
from src.routes.categorias import router as categorias_router

app = FastAPI(
    title="Sistema de Gestion de Inventario",
    description="REST API para el control de stock, abastecimientos y ventas.",
    version="1.0.0"
)

origins=[
    "http://localhost:3000",
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(categorias_router)
app.include_router(productos_router)
app.include_router(proveedores_router)
app.include_router(transacciones_router)



@app.get("/",tags=["Root"])
def read_root():
    return{
        "status":"Backend corriendo exitosamente",
        "proyecto":"Gestion de Inventario"
        }

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8080,reload=True)
