from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'user'

    s_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String,index=True)
    age = Column(Integer)

    