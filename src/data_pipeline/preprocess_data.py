import re
import string
import nltk
import os
import cv2
import numpy as np
from nltk.tokenize import word_tokenize
from PIL import Image

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

def clean_text(text):
    """
    Preprocesses the text by removing unnecessary characters and standardizing it.
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    
    # Remove special characters, numbers, and punctuations
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize text into words
    words = word_tokenize(text)
    
    return " ".join(words)

def preprocess_image(image_path, target_size=(224, 224)):
    """
    Preprocesses an image for model input by resizing and normalizing it.
    """
    image = Image.open(image_path)
    image = image.resize(target_size)  # Resize the image
    image_array = np.array(image)      # Convert to numpy array
    
    # Normalize pixel values
    image_array = image_array / 255.0
    
    return image_array

def preprocess_data(data):
    """
    Preprocesses the raw data (both text and images) into a format suitable for analysis and modeling.
    Args:
        data: List of dictionaries with 'type' (text/image), 'content' (text string or image file path)
    Returns:
        cleaned_data: List of processed content
    """
    cleaned_data = []
    
    for item in data:
        content_type = item['type']
        content = item['content']
        
        if content_type == 'text':
            cleaned_text = clean_text(content)
            cleaned_data.append({'type': 'text', 'content': cleaned_text})
        
        elif content_type == 'image':
            cleaned_image = preprocess_image(content)
            cleaned_data.append({'type': 'image', 'content': cleaned_image})
    
    return cleaned_data

# Example usage
data = [
    {'type': 'text', 'content': 'Check out these synthetic drugs for sale! http://example.com'},
    {'type': 'image', 'content': 'drug_image.jpg'}
]

cleaned_data = preprocess_data(data)
print(cleaned_data)
