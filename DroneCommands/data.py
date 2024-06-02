from flask import Flask
from flask_socketio import SocketIO
from djitellopy import Tello
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
tello = Tello()
tello.connect()

def get_tello_data():
    while True:
        temp = tello.get_temperature()
        battery = tello.get_battery()
        socketio.emit('drone_data', {'temperature': temp, 'battery': battery})
        time.sleep(5)

@app.route('/')
def index():
    return "Tello Drone Data API"

if __name__ == '__main__':
    data_thread = threading.Thread(target=get_tello_data)
    data_thread.daemon = True
    data_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
