from fastapi import FastAPI
from .routes import users, auth
from .database import Base, engine
from .routes import users, auth, clients

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(clients.router)