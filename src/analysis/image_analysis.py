import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load a pre-trained model for image classification (custom drug detection model)
model = load_model('drug_detection_model.h5')

# Function to preprocess the image
def preprocess_image(image_path):
    # Load image from path
    image = cv2.imread(image_path)
    
    # Resize image to the required size for the model (224x224 in this case)
    image_resized = cv2.resize(image, (224, 224))
    
    # Convert the image to a 4D tensor for prediction (batch_size, height, width, channels)
    image_array = np.expand_dims(image_resized, axis=0)
    
    # Normalize the pixel values to [0, 1]
    image_array = image_array / 255.0
    
    return image_array

# Function to classify the image
def analyze_image(image_path):
    # Preprocess the image
    image_array = preprocess_image(image_path)
    
    # Predict using the trained model
    prediction = model.predict(image_array)
    
    # If prediction is above threshold (0.5), it's suspicious
    if prediction[0] > 0.5:
        return "Suspicious Content"
    else:
        return "Not Suspicious"

# Example usage
if __name__ == "__main__":
    image_path = 'drug_image.jpg'  # Example image file path
    result = analyze_image(image_path)
    print(result)
