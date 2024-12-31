from db.database import stock_data_collection
from datetime import datetime

def fetch_latest_price(symbol: str):
    """Fetch the most recent price for a given symbol."""
    result = stock_data_collection.find({"symbol": symbol}).sort("timestamp", -1).limit(1)
    return next(result, None)

def fetch_all_data(symbol: str):
    """Fetch all data for a given symbol."""
    return list(stock_data_collection.find({"symbol": symbol}))

def insert_stock_data(symbol: str, price: float):
    """Insert a new stock data entry."""
    stock_data = {
        "symbol": symbol,
        "price": price,
        "timestamp": datetime.utcnow()
    }
    stock_data_collection.insert_one(stock_data)
    return stock_data