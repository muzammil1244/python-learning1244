from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



Base = declarative_base()



DATABASE_URL = "postgresql://postgres:muzammil1244@localhost:5432/rdata"

Database = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    bind= Database,
    autoflush=False

)

def get_db():

  db = sessionLocal()
  try:
    yield db
  finally:
    db.close()    

