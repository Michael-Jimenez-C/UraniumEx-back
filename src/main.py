from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import DataSchemes as sch
import DataBaseManagement as models
import crud
from DataBaseManagement import SessionLocal, engine
from auth import *
from datetime import datetime, timedelta, timezone

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/usuario')
async def signIn(user: sch.UsuarioCreate, db: Session = Depends(get_db)):
    user = crud.createUser(db, user = user)
    token = create_access_token({'n':user.nombres, 'a':user.apellidos},timedelta(minutes=30))
    return token

@app.get('/usuario', response_model=list[sch.UsuarioBase])
async def getUsuarios(skip:int = 0, limit:int = 100,db: Session = Depends(get_db)):
    return crud.getUsers(db,skip,limit)

@app.get('/usuario/{id}', response_model=sch.UsuarioBase)
async def getUsuario(id:int, db: Session = Depends(get_db)):
    user = crud.getUserbyId(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrada")
    return user

@app.put('/usuario', response_model=sch.UsuarioBase)
async def putUsuario():
    pass

@app.delete('/usuario/{id}')
async def delUsuario(id:int, db: Session = Depends(get_db)):
    eliminado = crud.removeUserById(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrada")
    return eliminado


@app.get('/asociacion',response_model=list[sch.Asociacion])
async def getAsociaciones(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.obtenerAsociaciones(db,skip,limit)

@app.get('/asociacion/{id}',response_model=list[sch.Asociacion])
async def getAsociacionPorId(id: int, db: Session = Depends(get_db)):
    asociacion = crud.obtenerAsociacionPorId(db,id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion no encontrada")
    return 

@app.post('/asociacion', response_model=sch.Asociacion)
async def postAsociacion(asociacion: sch.AsociacionCreate, db: Session = Depends(get_db)):
    return crud.crearAsociacion(db, asociacion)

@app.put('/asociacion')
async def putAsociacion(asociacion: sch.Asociacion, db:Session = Depends(get_db)):
    return crud.actualizarAsociacion(db,asociacion)

@app.get('/organizacion',response_model=list[sch.Organizacion])
async def getOrganizaciones(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.obtenerOrganizaciones(db,skip,limit)

@app.get('/organizacion/{id}',response_model=sch.Organizacion)
async def getOrganizacionPorId(id: int, db: Session = Depends(get_db)):
    organizacion = crud.obtenerOrganizacionPorId(db,id)
    if not organizacion:
        raise HTTPException(status_code=404, detail="Organizacion no encontrada")
    return organizacion

@app.post('/organizacion', response_model=sch.Organizacion)
async def postOrganizacion(organizacion: sch.OrganizacionCreate, db: Session = Depends(get_db)):
    return crud.crearOrganizacion(db, organizacion)

@app.put('/organizacion')
async def putOrganizacion(organizacion: sch.Organizacion, db:Session = Depends(get_db)):
    return crud.actualizarOrganizacion(db,organizacion)