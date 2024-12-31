# Secure Data Pipeline
A secure data pipeline with FastAPI for data ingestion and analysis.

## Features
- FastAPI for API endpoints
- MongoDB for database operations
- Pytest for testing
- Environment variable management with python-dotenv

## Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** for environment variables. Example:
   ```env
   MONGODB_URI=mongodb://localhost:27017/secure_data_pipeline
   API_KEY=your_finnhub_api_key
   HOST=127.0.0.1
   PORT=8000
   DEBUG=True
   ```

3. **Start the API**:
   ```bash
   uvicorn api.main:app --reload
   ```

## Testing
Run tests using pytest:
```bash
pytest tests/