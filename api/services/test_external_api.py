import sys
import os
from api.services.external_api import fetch_stock_data

# Ensure the project root is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../..")

symbol = 'AAPL'
try:
    data = fetch_stock_data(symbol)
    print(f'Stock data for {symbol}: {data}')
except ValueError as e:
    print(f'Error: {e}')
