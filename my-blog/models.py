from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    comment = Column(String)
    like = Column(Integer)
    post = Column(String)
    