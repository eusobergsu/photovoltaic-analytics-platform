from fastapi import FastAPI

from app.api.router import api_router

from app.core.database import engine, Base

from app.models.plant import Plant

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Photovoltaic Analytics Platform",
    version="0.1.0",
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "messege": "Photovoltaic Analytics Platform running"
    }