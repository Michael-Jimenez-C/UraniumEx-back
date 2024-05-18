from sqlalchemy.orm import Session
from routers.schemas.querySchemas import UserOrgs, UserOrgsWS, Org, Inv
from database.models.models import Usuario as usuario_model
from database.models.models import Asociacion as asociacion_model
from database.models.models import Organizacion as organizacion_model
from database.models.models import Inventario as inventario_model
from database.models.models import Stock as stock_model
from database.models.models import Producto as producto_model

def getUSerOrg(db : Session, user: UserOrgs):
    return db.query(organizacion_model).join(asociacion_model).join(usuario_model).filter(usuario_model.id == user.userid).all()

def getUserOrgByName(db : Session, user: UserOrgsWS):
    return db.query(organizacion_model).join(asociacion_model).join(usuario_model).filter(organizacion_model.nombre==user.nombreOrganizacion).first()

def getOrgInv(db: Session, org: Org):
    return db.query(inventario_model).join(organizacion_model).filter(organizacion_model.id == org.orgid).all()

def getInvProds(db: Session, inv: Inv):
    return db.query(producto_model).join(stock_model).join(inventario_model).filter(producto_model.id == inv.id).all()