# config.py

import os

# Paths
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, '..', 'data')
RAW_DATA_PATH = os.path.join(DATA_PATH, 'raw')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed')
MODEL_PATH = os.path.join(BASE_PATH, '..', 'models')

# Alert system settings
ALERT_THRESHOLD = 0.7  # Threshold for flagging suspicious content (e.g., 70% confidence for flagging posts)

# NLP Model parameters
NLP_MODEL_PATH = os.path.join(MODEL_PATH, 'nlp_model.pth')  # Path to the pre-trained NLP model
MAX_TEXT_LENGTH = 256  # Maximum text length for processing

# Image Model parameters
IMAGE_MODEL_PATH = os.path.join(MODEL_PATH, 'drug_detection_model.h5')  # Path to the image classification model

# Database settings
DATABASE_URI = "mongodb://localhost:27017/drug_trafficking_db"  # MongoDB URI for storing user profiles and flagged posts

# Logging settings
LOGGING_LEVEL = "INFO"  # Logging level (DEBUG, INFO, WARNING, ERROR)
LOG_FILE = os.path.join(BASE_PATH, 'app.log')  # Path for storing logs

# API settings
API_KEY = "your_api_key_here"  # API key for accessing platform services (if applicable)
