from fastapi import FastAPI, Request, Response, status, HTTPException, Depends
from .database import engine
from . import models
from .routers import post, user, auth, vote, db
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware


# if using "alembic" 
# this statement not required
# models.Base.metadata.create_all(bind=engine)

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



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
# app.include_router(vote.router)
app.include_router(db.router)


@app.get('/')
def root():
    return {"message":"Hello Word"}

