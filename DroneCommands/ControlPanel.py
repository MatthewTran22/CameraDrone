import cv2
import tkinter as tk
from djitellopy import Tello
from threading import Thread
from PIL import Image, ImageTk

class TelloVideoStream:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()
        self.tello.streamon()
        self.frame = None
        self.stop_stream = False

        # Start the video stream thread
        self.stream_thread = Thread(target=self.update_frame, daemon=True)
        self.stream_thread.start()

    def update_frame(self):
        while not self.stop_stream:
            self.frame = self.tello.get_frame_read().frame

    def get_frame(self):
        return self.frame

    def release(self):
        self.stop_stream = True
        self.tello.streamoff()
        self.tello.end()

class DroneControlPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TELLO DRONE CONTROL PANEL")

        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set window size to 80% of screen width and height
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        # Set the geometry of the main window
        self.geometry(f"{window_width}x{window_height}")

        # Set the background color of the main window to dark gray
        self.configure(bg="darkgray")

        # Create a frame that takes 60% of the main window height and 100% of its width
        inner_frame_height = int(window_height * 0.6)
        inner_frame = tk.Frame(self, width=window_width, height=inner_frame_height, bg="gray")
        inner_frame.place(x=0, y=0)  # Place at the top of the window

        # Create a frame that takes the bottom 40% of the main window
        bottom_frame_height = int(window_height * 0.4)
        bottom_frame = tk.Frame(self, width=window_width, height=bottom_frame_height, bg="darkgray")
        bottom_frame.place(x=0, y=inner_frame_height)

        # Initialize labels inside the bottom frame
        self.battery_label = tk.Label(bottom_frame, text="Battery Level: ", bg="darkgray", fg="white")
        self.battery_label.pack(side=tk.BOTTOM, anchor='s', pady=5)

        self.flight_time_label = tk.Label(bottom_frame, text="Flight Time: ", bg="darkgray", fg="white")
        self.flight_time_label.pack(side=tk.BOTTOM, anchor='s', pady=5)

        self.temperature_label = tk.Label(bottom_frame, text="Temperature: ", bg="darkgray", fg="white")
        self.temperature_label.pack(side=tk.BOTTOM, anchor='s', pady=5)

        # Initialize the Tello video stream
        self.tello_video = TelloVideoStream()

        # Start the video update loop
        self.update_video_feed()

    def update_video_feed(self):
        frame = self.tello_video.get_frame()
        if frame is not None:
            # Display the frame using OpenCV
            cv2.imshow("Tello Video Feed", frame)
            cv2.waitKey(1)

        # Schedule the next update
        self.after(33, self.update_video_feed)  # Update at ~30 FPS

    def on_closing(self):
        self.tello_video.release()
        cv2.destroyAllWindows()
        self.destroy()

    def update_labels(self):
        # Update the labels with the drone data
        self.battery_label.config(text=f"Battery Level: {self.tello_video.tello.get_battery()}%")
        self.flight_time_label.config(text=f"Flight Time: {self.tello_video.tello.get_flight_time()} minutes")
        self.temperature_label.config(text=f"Temperature: {self.tello_video.tello.get_highest_temperature()}F")

        # Schedule the next update
        self.after(1000, self.update_labels)  # Update every second

if __name__ == "__main__":
    app = DroneControlPanel()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.update_labels()
    app.mainloop()
