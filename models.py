from sqlalchemy import Column , Integer, String 
from database import Base

class BookModel(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key = True, index= True)
    name = Column(String(100), nullable = False)
    author = Column(String(100), nullable = False)
    isbn = Column(String(13),unique = True, nullable = False)
    genre = Column(String(20), nullable = False)
    
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    