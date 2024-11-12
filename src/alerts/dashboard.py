from flask import Flask, render_template, request
import os

# Sample data (can be fetched from a database)
alerts_data = [
    {
        "timestamp": "2024-11-12 10:20:15",
        "post_content": "Synthetic drugs available for sale.",
        "user_id": "user123",
        "post_type": "Text"
    },
    {
        "timestamp": "2024-11-12 11:45:30",
        "post_content": "Order drugs online anonymously.",
        "user_id": "user456",
        "post_type": "Image"
    },
]

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage of the dashboard."""
    return render_template('index.html', alerts=alerts_data)

@app.route('/view_alert', methods=['GET'])
def view_alert():
    """View detailed information about a specific alert."""
    alert_id = request.args.get('alert_id', type=int)
    alert = alerts_data[alert_id] if alert_id is not None else None
    return render_template('view_alert.html', alert=alert)

if __name__ == "__main__":
    app.run(debug=True)
