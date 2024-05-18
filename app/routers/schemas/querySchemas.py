from pydantic import BaseModel


class UserOrgs(BaseModel):
    userid: int

class UserOrgsWS(UserOrgs):
    nombreOrganizacion:str

class Org(BaseModel):
    orgid:int

class Inv(BaseModel):
    id:int