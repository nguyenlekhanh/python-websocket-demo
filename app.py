from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event handler for new connections
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    emit('response', {'data': 'Message received!'})

# Run the Flask app with SocketIO support
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
