from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url_object = URL.create(
#     "mysql",
#     username="root",
#     password="secret",
#     host="localhost:33060",
#     database="DBAP",
# )

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Connection:
    instancia = None
    def get_db():
        if not Connection.instancia:
            Connection.instancia =SessionLocal()
        return Connection.instancia

def get_db():
    return Connection.get_db()