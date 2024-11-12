# anomaly_detection.py

from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd

def detect_anomalies(user_activity_data):
    """
    user_activity_data: A DataFrame with columns like 'user_id', 'activity_score', 'timestamp', etc.
    The 'activity_score' could represent various metrics, such as the frequency of posts, flagged content, etc.
    """
    # Convert relevant features into a numpy array for clustering
    features = user_activity_data[['activity_score', 'timestamp']].values
    
    # Apply DBSCAN (Density-Based Spatial Clustering of Applications with Noise) for anomaly detection
    model = DBSCAN(eps=0.5, min_samples=5)  # eps: maximum distance between samples, min_samples: min samples per cluster
    user_activity_data['anomaly'] = model.fit_predict(features)
    
    # -1 indicates an outlier or anomaly
    anomalous_users = user_activity_data[user_activity_data['anomaly'] == -1]
    return anomalous_users

# Example usage
if __name__ == "__main__":
    # Sample data: Replace with actual user activity data
    data = {
        'user_id': [1, 2, 3, 4, 5],
        'activity_score': [5, 100, 50, 500, 10],
        'timestamp': [1620000000, 1620000500, 1620001000, 1620001500, 1620002000]
    }
    
    user_activity_df = pd.DataFrame(data)
    anomalous_users = detect_anomalies(user_activity_df)
    
    print("Anomalous Users:")
    print(anomalous_users)
