import tkinter as tk
from tkinter import ttk
from threading import Thread
import socketio

# Connect to the Flask-SocketIO server
sio = socketio.Client()
sio.connect('http://localhost:5000')

class TelloDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tello Drone Data")
        
        self.temperature_label = ttk.Label(root, text="Temperature: N/A")
        self.temperature_label.pack(pady=10)
        
        self.battery_label = ttk.Label(root, text="Battery: N/A")
        self.battery_label.pack(pady=10)
        
        # Start a background thread to update the GUI with drone data
        self.update_thread = Thread(target=self.update_data)
        self.update_thread.daemon = True
        self.update_thread.start()
        
    def update_data(self):
        @sio.event
        def connect():
            print("Connected to the server")
        
        @sio.event
        def disconnect():
            print("Disconnected from the server")
        
        @sio.on('drone_data')
        def on_drone_data(data):
            temperature = data['temperature']
            battery = data['battery']
            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.battery_label.config(text=f"Battery: {battery}%")
        
        # Start the event loop
        sio.wait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelloDataGUI(root)
    root.mainloop()
