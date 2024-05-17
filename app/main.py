from fastapi import FastAPI
from database.connection import engine, Base
from routers import usuario, organizacion, asociacion, inventario, producto, stock

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(usuario.router)
app.include_router(organizacion.router)
app.include_router(asociacion.router)
app.include_router(inventario.router)
app.include_router(stock.router)
app.include_router(producto.router)

@app.get("/")
async def checkhealth():
    return {"message": "Hi :D"}