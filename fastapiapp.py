from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib


app = FastAPI()

@app.post("/predict")