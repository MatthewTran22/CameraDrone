import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading

def get_screen_dimensions():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def update_camera_feed(camera_label):
    cap = cv2.VideoCapture(0)

    def show_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            camera_label.imgtk = imgtk
            camera_label.configure(image=imgtk)
        camera_label.after(10, show_frame)
    
    show_frame()

def create_main_window():
    screen_width, screen_height = get_screen_dimensions()
    
    # Calculate window dimensions (70% of screen size)
    window_width = int(screen_width * 0.7)
    window_height = int(screen_height * 0.7)
    
    # Create the main window
    root = tk.Tk()
    root.title("Camera Display Window")
    
    # Set window size and position
    root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
    
    # Create a frame for the camera display box
    camera_frame = ttk.Frame(root, width=window_width, height=int(window_height * 0.7))
    camera_frame.pack_propagate(False) # Prevent the frame from resizing to its contents
    camera_frame.pack(fill=tk.X, side=tk.TOP)
    
    # Create a label to hold the camera feed
    camera_label = tk.Label(camera_frame, bg="light gray")
    camera_label.pack(fill=tk.BOTH, expand=True)
    
    # Start the camera feed in a separate thread
    threading.Thread(target=update_camera_feed, args=(camera_label,), daemon=True).start()
    
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
