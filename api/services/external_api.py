import os
import requests
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("API_KEY")
FINNHUB_BASE_URL = "https://finnhub.io/api/v1"

def fetch_stock_data(symbol: str):
    """
    Fetch stock data for a given symbol from Finnhub API.
    """
    if not FINNHUB_API_KEY:
        raise ValueError("Finnhub API key is not configured in the environment variables.")

    url = f"{FINNHUB_BASE_URL}/quote"
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from Finnhub: {response.json()}")

    return response.json()