from fastapi import APIRouter, HTTPException
from db.database import stock_data_collection

router = APIRouter()

@router.get("/average-price")
def get_average_price(symbol: str):
    # Fetch all documents for the given symbol
    stock_data = list(stock_data_collection.find({"symbol": symbol}))

    if not stock_data:
        raise HTTPException(status_code=404, detail=f"No data found for symbol {symbol}")

    # Calculate average price
    average_price = sum(item["price"] for item in stock_data) / len(stock_data)
    return {"symbol": symbol, "average_price": average_price}

@router.get("/latest-price")
def get_latest_price(symbol: str):
    # Fetch the latest document for the given symbol
    result = stock_data_collection.find({"symbol": symbol}).sort("timestamp", -1).limit(1)
    latest_data = next(result, None)

    if not latest_data:
        raise HTTPException(status_code=404, detail=f"No data found for symbol {symbol}")

    return {
        "symbol": symbol,
        "latest_price": latest_data["price"],
        "timestamp": latest_data["timestamp"]
    }

@router.get("/latest-prices")
def get_latest_prices():
    # Fetch the latest price for all stocks
    pipeline = [
        {"$sort": {"timestamp": -1}},  # Sort by timestamp descending
        {"$group": {"_id": "$symbol", "latest_price": {"$first": "$price"}, "timestamp": {"$first": "$timestamp"}}}
    ]
    results = list(stock_data_collection.aggregate(pipeline))

    if not results:
        raise HTTPException(status_code=404, detail="No data found.")

    # Format the results
    response = [
        {"symbol": item["_id"], "latest_price": item["latest_price"], "timestamp": item["timestamp"]}
        for item in results
    ]
    return response