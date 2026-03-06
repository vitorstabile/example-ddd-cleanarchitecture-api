# app/main.py
from fastapi import FastAPI
from app.presentation.controllers.user_controller import router as user_router

app = FastAPI(title="Simple API", version="0.1.0")

# The router is included, and since the controller imports from 
# dependencies.py, the circular loop is broken.
app.include_router(user_router, prefix="/user", tags=["User Search"])

@app.get("/")
def root():
    return {"message": "Simple API is running"}