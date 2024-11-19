# Makefile

# Define the FRED_API_KEY
FRED_API_KEY=9fa08a80b2356aa126ed2254c6bb9e8c

# Define a target to run your Python script
run-script:
    @echo "Running the Python script with FRED API Key"
    FRED_API_KEY=$(FRED_API_KEY) python your_script.py
