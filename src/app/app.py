from flask import Flask, request, jsonify
from api_routes import api_routes  # Import the route handlers

# Initialize Flask app
app = Flask(__name__)

# Register routes from the api_routes.py file
app.register_blueprint(api_routes)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
