from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API", version="0.1.0")

app.include_router(router)

@app.get("/api")
def read_root():
    return {"message": "Hello World"}