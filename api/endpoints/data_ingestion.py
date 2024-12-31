import os
import requests
from datetime import datetime
from fastapi import APIRouter, HTTPException
from db.database import stock_data_collection

router = APIRouter()

FINNHUB_API_KEY = os.getenv("API_KEY")
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"

@router.post("/add-test-data")
def add_test_data():
    test_data = {
        "symbol": "AAPL",
        "price": 150.25,
        "timestamp": datetime.utcnow()
    }
    stock_data_collection.insert_one(test_data)
    return {"message": "Test data added to MongoDB"}

@router.post("/fetch-stock-data")
def fetch_stock_data(symbol: str):
    # Validate API key
    if not FINNHUB_API_KEY:
        raise HTTPException(status_code=500, detail="Finnhub API key not configured.")

    # Fetch stock data from Finnhub
    url = f"{FINNHUB_BASE_URL}/quote"
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, 
            detail=f"Failed to fetch data from Finnhub: {response.json()}"
        )

    data = response.json()
    # Prepare document to save in MongoDB
    stock_data = {
        "symbol": symbol,
        "price": data.get("c"),  # Current price
        "timestamp": datetime.utcnow()
    }

    # Save to MongoDB
    stock_data_collection.insert_one(stock_data)
    return {"message": f"Stock data for {symbol} saved successfully!"}