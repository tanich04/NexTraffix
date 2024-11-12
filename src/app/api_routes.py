from flask import Blueprint, request, jsonify
from src.analysis.text_analysis import analyze_text
from src.analysis.image_analysis import analyze_image
from src.alerts.alert_system import generate_alert
from src.network_analysis.network_graph import analyze_network

# Initialize a Flask Blueprint for the API
api_routes = Blueprint('api_routes', __name__)

# Route to analyze a text post
@api_routes.route('/analyze_text', methods=['POST'])
def analyze_text_route():
    try:
        data = request.get_json()
        post_text = data.get('text', '')  # Extract the text data from request
        
        if not post_text:
            return jsonify({"error": "Text is required"}), 400
        
        result = analyze_text(post_text)  # Analyze the text content
        response = {
            "message": "Text analysis complete",
            "result": "Suspicious" if result == 1 else "Not Suspicious"
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to analyze an image post
@api_routes.route('/analyze_image', methods=['POST'])
def analyze_image_route():
    try:
        file = request.files['image']  # Get the image file from the request
        if not file:
            return jsonify({"error": "Image file is required"}), 400

        # Save the image temporarily for processing
        image_path = './temp_images/' + file.filename
        file.save(image_path)

        result = analyze_image(image_path)  # Analyze the image content
        response = {
            "message": "Image analysis complete",
            "result": result
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to analyze a user network for suspicious connections
@api_routes.route('/analyze_network', methods=['POST'])
def analyze_network_route():
    try:
        data = request.get_json()
        user_data = data.get('user_data', {})  # Get the user interaction data
        
        if not user_data:
            return jsonify({"error": "User data is required"}), 400
        
        clusters = analyze_network(user_data)  # Detect suspicious network clusters
        response = {
            "message": "Network analysis complete",
            "clusters": clusters
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to generate real-time alerts based on suspicious activity
@api_routes.route('/generate_alert', methods=['POST'])
def generate_alert_route():
    try:
        data = request.get_json()
        activity = data.get('activity', '')  # Suspicious activity description
        
        if not activity:
            return jsonify({"error": "Activity description is required"}), 400
        
        alert = generate_alert(activity)  # Generate the alert based on activity
        response = {
            "message": "Alert generated successfully",
            "alert": alert
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
