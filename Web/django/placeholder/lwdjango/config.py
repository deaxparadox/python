import os
from pydantic import BaseSettings

class envs(BaseSettings):
    DEBUG: str
    SECRET: bytes = os.urandom(32)
    ALLOWED_HOSTS: str 
    
    class Config:
        env_file: str = ".env"
        
env = envs()
# print(env.SECRET)