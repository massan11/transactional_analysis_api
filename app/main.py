from fastapi import FastAPI
from .database import engine, Base
from .routes import users

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Transactional Analysis API"}
