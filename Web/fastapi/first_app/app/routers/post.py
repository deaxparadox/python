from typing import Optional, List
from fastapi import FastAPI, Request, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, utils, oauth2
from ..database  import get_db


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

'''GET ALL POST'''
# @router.get('/all', response_model=List[schemas.Post])
@router.get('/all', response_model=List[schemas.VoteCount])
def get_posts(
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user),
        limit: int = None,
        title: str = None,
        skip: int = 0,
        search: Optional[str] = ""
    ):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    post_query = db.query(
        models.Post, func.count(models.Votes.post_id).label("votes")
        ).join(
            models.Votes, models.Votes.post_id == models.Post.id, isouter=True
            ).group_by(
                models.Post.id
                ).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
            
    print(post_query)
    # return posts
    return post_query


"""GET USER POST"""
@router.get('/', response_model=List[schemas.VoteCount])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(
        models.Post, func.count(models.Votes.post_id).label("votes")
        ).join(
            models.Votes, models.Votes.post_id == models.Post.id, isouter=True
            ).group_by(
                models.Post.id
                ).filter(models.Post.owner_id == current_user.id).all()
    return posts


"""POST POST"""
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


"""GET POST BY ID"""
@router.get('/{id}', response_model=schemas.VoteCount)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post =  db.query(
        models.Post, func.count(models.Votes.post_id).label("votes")
        ).join(
            models.Votes, models.Votes.post_id == models.Post.id, isouter=True
            ).group_by(
                models.Post.id
                ).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"post with id: {id} was not found"
        )
    return post
    

"""DELETING POST BY ID"""
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):   
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not found"
        )    
        
    # cannot delete if not owner
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


"""UPDATING POST BY ID"""
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist"
        )
        
    # cannot delete if not owner
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
        
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


