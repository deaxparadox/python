from typing import Optional, List, Any, Set
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from fastapi import Path

'''declare validation and metadata using "Field" '''

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str 
    description: Optional[str] = None 
    price: float 
    tax: Optional[float] = None 
    tags: List[str] = []
    
class UserIn(BaseModel):
    username: str 
    password: str 
    email: EmailStr
    full_name: Optional[str] = None 
    
    
class UserOut(BaseModel):
    username: str 
    email: EmailStr
    full_name: Optional[str] = None

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(
#         ...,
#         gt=0,
#         description="The price must be greator than zero"
#     )
#     tax: Optional[float] = None
#     # tags: List[Any] = []
#     # tags: Set[str] = set()
#     # image: Optional[Image] = None           # submodel as a type
#     # image: Optional[List[Image]] = None         # List of submodel
    
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": .2
#             }
#         }
    
    
    
class Offer(BaseModel):
    name: str 
    description: Optional[str] = None 
    price: float 
    items: List[Item]

class ItemUser(BaseModel):
    username: str 
    full_name: str
    
    
class Universal(BaseModel):
    firstname: str 
    lastname: str 
    age: int 
    email: EmailStr
    phone: int 