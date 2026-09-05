from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, StrictFloat, StrictInt
from typing import Union

app = FastAPI(title="student-ml-api")

VERSION_FILE = Path(__file__).resolve().parent / "VERSION"

def get_app_version() -> str:
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text().strip()
    return "1.0.0"

class PredictionRequest(BaseModel):
    value: Union[StrictInt, StrictFloat]

class PredictionResponse(BaseModel):
    input: Union[StrictInt, StrictFloat]
    prediction: Union[StrictInt, StrictFloat]

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": get_app_version()
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    return {"input": payload.value, "prediction": payload.value * 10}