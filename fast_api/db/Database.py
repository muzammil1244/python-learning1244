from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:muzammil1244@localhost:5432/first_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
)

# dependancy 

def get_db():

  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()        