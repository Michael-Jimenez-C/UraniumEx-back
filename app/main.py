from fastapi import FastAPI
from app.database.connection import engine, Base
from app.routers import usuario, organizacion, asociacion

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(usuario.router)
app.include_router(organizacion.router)
app.include_router(asociacion.router)

@app.get("/")
async def checkhealth():
    return {"message": "Hi :D"}