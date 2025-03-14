from fastapi import FastAPI
from .database import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Transactional Analysis API"}
