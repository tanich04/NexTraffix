# helpers.py

import logging
import os
from datetime import datetime
import json

# Set up logging
def setup_logging(log_file='app.log', log_level="INFO"):
    log_level_dict = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
    }
    
    log_level = log_level_dict.get(log_level, logging.INFO)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Function to save JSON data
def save_json(data, file_path):
    """Save a Python dictionary to a JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to load JSON data
def load_json(file_path):
    """Load data from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        logging.warning(f"File not found: {file_path}")
        return None

# Function to preprocess text data (example)
def preprocess_text(text):
    """Basic text preprocessing: remove non-alphanumeric characters, lowercase the text."""
    return ''.join(e for e in text if e.isalnum()).lower()

# Example of a custom exception for handling errors
class CustomException(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.status_code = status_code

# Helper function for timestamping data entries
def timestamp_data(data):
    """Add timestamp to data entries."""
    timestamp = datetime.utcnow().isoformat()
    if isinstance(data, dict):
        data['timestamp'] = timestamp
    else:
        data = {'data': data, 'timestamp': timestamp}
    return data
