from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from fastapi import Path

class Item(BaseModel):
    name: str 
    description: Optional[str] = None 
    price: float 
    tax: Optional[float] = None 
    tags: List[str] = []
    
    
class UserOut(BaseModel):
    username: str 
    email: EmailStr
    full_name: Optional[str] = None
    

class UniversalOuput(BaseModel):
    firstname: str 
    lastname: str 
    age: int 
    email: EmailStr
    phone: int 
    
    class Config:
        orm_mode = True
        
class UserUniversalOuput(BaseModel):
    firstname: str 
    lastname: str 
    age: int 
    email: EmailStr
    phone: int 
    user_id: int 
    
    class Config:
        orm_mode = True