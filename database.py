from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

db_URL = "sqlite:///students.db"
engine = create_engine(db_URL, connect_args = {"check_same_thread": False})

sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try: 
        yield db
    finally:
        db.close()