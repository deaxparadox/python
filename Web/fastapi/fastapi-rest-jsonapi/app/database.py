
# DATABASE
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import QueuePool
from . import model

engine: Engine = create_engine(
    "sqlite:///:memory:",
    poolclass=QueuePool,
    connect_args={
    "check_same_thread":False
    }
)

model.User.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

def generate_users(COUNT: int = 10):
    for i in range(COUNT):
        user = model.User(name=f"User {i}", age=i)
        session.add(user)
    session.commit()
generate_users()

