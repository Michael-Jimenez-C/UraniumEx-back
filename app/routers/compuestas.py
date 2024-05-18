from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas.querySchemas import UserOrgs, UserOrgsWS, Org, Inv
from database.crud import compuestas as crud
from database.connection import get_db

router = APIRouter(
    prefix="/get",
    tags=["get"],
)

@router.post('/orgs')
async def get(user: UserOrgs, db: Session = Depends(get_db)):
    return crud.getUSerOrg(db, user)

@router.post('/org')
async def get1(user: UserOrgsWS, db: Session = Depends(get_db)):
    return crud.getUserOrgByName(db, user)

@router.post('/invs')
async def get2(org: Org, db:Session = Depends(get_db)):
    return crud.getOrgInv(db,org)

@router.post('/prod')
async def get2(inv: Inv, db:Session = Depends(get_db)):
    return crud.getInvProds(db,inv)