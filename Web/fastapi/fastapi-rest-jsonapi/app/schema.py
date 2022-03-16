
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
from . import database, model, app

class UserList(ResourceList):
    schema = UserSchema
    data_layer = SQLAlchemyDataLayer(database.session, model.User)
    
class UserDetail(ResourceDetail):
    __view_parameters__ = {"id": (int, Path(..., title="id", ge=1))}
    schema = UserSchema
    data_layer = SQLAlchemyDataLayer(model.session, model.User)
    
app.rest_api.register(UserList, "/users")
app.rest_api.register(UserDetail, "/users/{id}")