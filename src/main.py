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


@app.post('/usuarios/add')
async def signIn(user: sch.UsuarioC, db: Session = Depends(get_db)):
    user = crud.createUser(db, user = user)
    return create_access_token({'n':user.nombres, 'a':user.apellidos},timedelta(minutes=30))

@app.get('/usuarios', response_model=list[sch.UsuarioGet])
async def getUsuarios(skip:int = 0, limit:int = 100,db: Session = Depends(get_db)):
    return crud.getUsers(db,skip,limit)

@app.get('/usuarios/{id}', response_model=sch.UsuarioGet)
async def getUsuarios(id:int, db: Session = Depends(get_db)):
    user = crud.getUserbyId(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete('/usuarios/')
async def delUsuarios():
    pass

@app.put('/usuarios')
async def putUsuarios():
    pass