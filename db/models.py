from pydantic import BaseModel
from datetime import datetime

class StockData(BaseModel):
    symbol: str
    price: float
    timestamp: datetime