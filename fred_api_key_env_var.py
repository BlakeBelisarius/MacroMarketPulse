import os
from fredapi import Fred
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from environment variables
FRED_API_KEY = os.getenv('FRED_API_KEY')

# Check if the API key was loaded successfully
if FRED_API_KEY is None:
    raise ValueError("FRED_API_KEY is not set or could not be loaded.")
else:
    print(f"FRED_API_KEY is loaded: {FRED_API_KEY[:4]}...")  # Print only first few chars for verification

# Initialize Fred API instance
fred = Fred(api_key=FRED_API_KEY)

#9fa08a80b2356aa126ed2254c6bb9e8c