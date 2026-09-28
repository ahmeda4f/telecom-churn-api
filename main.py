from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
from contextlib import asynccontextmanager

ml_models = {}
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        ml_models["churn_pipeline"] = joblib.load("churn_prediction_pipeline.pkl")
        print("Model pipeline loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
    yield
    ml_models.clear()

app = FastAPI(title="Churn Prediction API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
async def predict_churn(customer: CustomerData):
    try:
        input_data = pd.DataFrame([customer.model_dump()])
        pipeline = ml_models["churn_pipeline"]
        churn_prob = pipeline.predict_proba(input_data)[0][1]
      
        if churn_prob < 0.40:
            risk_segment = "Low Risk"
        elif churn_prob < 0.70:
            risk_segment = "Medium Risk"
        else:
            risk_segment = "High Risk"
            
        return {
            "churn_probability": round(float(churn_prob), 4),
            "risk_segment": risk_segment,
            "intervention_recommended": risk_segment == "High Risk"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
