from typing import Optional, List
from fastapi import FastAPI, Request, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database  import get_db


router = APIRouter(
    prefix="/db",
    tags=["Database"]
)

"""database search"""
@router.get('/',)
def inner_join(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    print("database response root")
    return {"topic": "db root"}


"""INNER JOIN users and posts"""
@router.get('/inner',)
def inner_join(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    print("database response root")
    return {"topic": "innerjoin"}