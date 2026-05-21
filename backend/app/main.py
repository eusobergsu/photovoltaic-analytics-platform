from fastapi import FastAPI

app = FastAPI(
    title="Photovoltaic Analytics Platform",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "messege": "Photovoltaic Analytics Platform running"
    }