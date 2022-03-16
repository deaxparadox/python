
# MODEL 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
