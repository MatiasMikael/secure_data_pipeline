from fastapi import FastAPI
from api.endpoints.data_ingestion import router as data_ingestion_router
from api.endpoints.data_analysis import router as data_analysis_router

app = FastAPI()

app.include_router(data_ingestion_router, prefix="/data-ingestion", tags=["Data Ingestion"])
app.include_router(data_analysis_router, prefix="/data-analysis", tags=["Data Analysis"])

@app.get("/")
def root():
    return {"message": "Secure Data Pipeline API"}