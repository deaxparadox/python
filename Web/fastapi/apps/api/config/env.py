from pydantic import BaseSettings
import os

class envs(BaseSettings):
    TODO_DB_NAME: str
    TODO_DB_USERNAME: str
    TODO_DB_PASSWORD: str
    TODO_DB_HOST: str
    TODO_DB_PORT: str
    SECRET_KEY = os.urandom(32)
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES:str
    
    class Config:
        env_file=".env"

env = envs()