import os
from flask import Flask
from flask_socketio import SocketIO

# Create Flask app and initialize SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins, adjust for production

@app.route('/')
def index():
    return "Hello, Flask-SocketIO!"

# Event: Handle a simple WebSocket message
@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    socketio.send("Message received!")

# Running the Flask-SocketIO app
if __name__ == '__main__':
    # Use the environment variable PORT or default to 5000
    port = int(os.environ.get('PORT', 5000))

    # Print the server port for debugging
    print(f"Server running on port: {port}")
    
    # Run the app (bind to all available IP addresses and use the dynamic port)
    socketio.run(app, host='0.0.0.0', port=port, ssl_context='adhoc')  # For SSL (https)
