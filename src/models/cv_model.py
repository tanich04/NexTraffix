# cv_model.py

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load pre-trained model (you can train your own model or use a pre-trained object detection model)
model = load_model('drug_detection_model.h5')  # Replace with your actual model

def preprocess_image(img_path):
    # Load image and resize it for the model
    img = image.load_img(img_path, target_size=(224, 224))  # Resize to model input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize the image
    return img_array

def analyze_image(img_path):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)
    
    # Assuming the model outputs a value representing suspicious content (0 - not suspicious, 1 - suspicious)
    if prediction[0] > 0.5:
        return "Suspicious Content"
    else:
        return "Not Suspicious"

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess frame
        frame_resized = cv2.resize(frame, (224, 224))
        frame_array = np.expand_dims(frame_resized, axis=0) / 255.0
        
        prediction = model.predict(frame_array)
        label = "Suspicious Content" if prediction[0] > 0.5 else "Not Suspicious"
        
        # Display the frame with the label
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage
    img_path = 'drug_image.jpg'  # Replace with actual image path
    result = analyze_image(img_path)
    print(result)

    video_path = 'drug_video.mp4'  # Replace with actual video path
    analyze_video(video_path)
