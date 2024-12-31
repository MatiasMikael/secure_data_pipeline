from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)

# Define the database and collection
db = client["secure_data_pipeline"]
stock_data_collection = db["stock_data"]