from fastapi import FastAPI
from fastapi_rest_jsonapi import RestAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://www.google.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)


rest_api = RestAPI(app)


# MODEL 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    

# DATABASE
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import QueuePool

engine: Engine = create_engine(
    "sqlite:///:memory:",
    poolclass=QueuePool,
    connect_args={
    "check_same_thread":False
    }
)

User.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

def generate_users(COUNT: int = 10):
    for i in range(COUNT):
        user = User(name=f"User {i}", age=i)
        session.add(user)
    session.commit()
generate_users()


# SCHEMA and RESOURCES
from fastapi_rest_jsonapi.schema import fields, Schema

class UserSchema(Schema):
    __type__ = "user"
    
    id = fields.Integer()
    name = fields.String()
    age = fields.Integer()
    

from fastapi import Path
from fastapi_rest_jsonapi.resource import ResourceDetail, ResourceList
from fastapi_rest_jsonapi.data import SQLAlchemyDataLayer

class UserList(ResourceList):
    schema = UserSchema
    data_layer = SQLAlchemyDataLayer(session, User)
    
class UserDetail(ResourceDetail):
    __view_parameters__ = {"id": (int, Path(..., title="id", ge=1))}
    schema = UserSchema
    data_layer = SQLAlchemyDataLayer(session, User)
    
rest_api.register(UserList, "/users")
rest_api.register(UserDetail, "/users/{id}")