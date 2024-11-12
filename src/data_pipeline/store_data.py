import os
import pickle
import json
import numpy as np

# Directory paths
TEXT_DATA_DIR = 'data/processed/text_data/'
IMAGE_DATA_DIR = 'data/processed/image_data/'

def store_text_data(text_data, file_name):
    """
    Stores the preprocessed text data in a file.
    Args:
        text_data: The cleaned text data to be stored.
        file_name: The name of the file where the data will be stored.
    """
    if not os.path.exists(TEXT_DATA_DIR):
        os.makedirs(TEXT_DATA_DIR)
    
    file_path = os.path.join(TEXT_DATA_DIR, file_name)
    
    with open(file_path, 'w') as f:
        json.dump(text_data, f)
    
    print(f"Text data saved to {file_path}")

def store_image_data(image_data, file_name):
    """
    Stores the preprocessed image data as a numpy array.
    Args:
        image_data: The cleaned image data (numpy array).
        file_name: The name of the file where the image will be stored.
    """
    if not os.path.exists(IMAGE_DATA_DIR):
        os.makedirs(IMAGE_DATA_DIR)
    
    file_path = os.path.join(IMAGE_DATA_DIR, file_name)
    
    # Save as numpy binary format
    np.save(file_path, image_data)
    
    print(f"Image data saved to {file_path}")

def store_data(processed_data):
    """
    Stores all the preprocessed data (text and images) into their respective locations.
    Args:
        processed_data: A list of processed content (text or image).
    """
    for idx, item in enumerate(processed_data):
        content_type = item['type']
        content = item['content']
        
        if content_type == 'text':
            store_text_data(content, f"text_{idx}.json")
        
        elif content_type == 'image':
            store_image_data(content, f"image_{idx}.npy")

# Example usage
store_data([
    {'type': 'text', 'content': 'Check out these synthetic drugs for sale!'},
    {'type': 'image', 'content': np.random.rand(224, 224, 3)}  # Simulated image data
])
