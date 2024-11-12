import re
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load a pre-trained BERT model for sequence classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Function to preprocess and clean the text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions (@username)
    text = re.sub(r'#\w+', '', text)     # Remove hashtags (#hashtag)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text

# Function to classify the text
def analyze_text(post_text):
    # Clean the text
    cleaned_text = clean_text(post_text)
    
    # Tokenize and encode the text
    inputs = tokenizer(cleaned_text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    
    # Run the model
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1)  # Get the class with the highest score
    
    # 1 -> Suspicious, 0 -> Not Suspicious
    return prediction.item()

# Example usage
if __name__ == "__main__":
    post = "Get your synthetic drugs here! Contact me via encrypted message."
    result = analyze_text(post)
    print("Suspicious Post" if result == 1 else "Not Suspicious")
