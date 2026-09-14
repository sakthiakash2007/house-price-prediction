import joblib
from fastapi import FastAPI
from pathlib import Path
model = joblib.load("deployment/model.pkl")
joblib.dump(model,"deployment\model.pkl")
print("model saved from deployment ")
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("deployment/model.pkl")


class HouseData(BaseModel):
    Area: float
    Bedrooms: int
    Bathrooms: int
    Age: int
    Distance_City: float


@app.post("/predict")
def predict(data: HouseData):

    values = [[
        data.Area,
        data.Bedrooms,
        data.Bathrooms,
        data.Age,
        data.Distance_City
    ]]

    prediction = model.predict(values)

    return {"predicted_price": float(prediction[0])}