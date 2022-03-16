from fastapi import FastAPI, Query, HTTPException
from typing import Optional, List
from .config import models

app= FastAPI()

@app.get('/todo/')
async def get_todo(todo: models.Todo):
    
    return todo.dict()