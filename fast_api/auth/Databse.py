from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker




DATABASE_URL = "postgresql://postgres:muzammil1244@localhost:5432/auth"
engine = create_engine(DATABASE_URL)



Base = declarative_base()

sessionLocal  = sessionmaker(
    bind=engine,
    expire_on_commit=False
)


# dependency

def get_db ():
    db = sessionLocal()
    try :
       yield  db
    finally:
        db.close()