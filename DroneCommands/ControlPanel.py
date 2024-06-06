import tkinter as tk
from data import get_drone_status, get_battery_level, get_flight_time, get_temp  # Import the functions from the other Python file

def update_labels():
    # Fetch drone data from another file
    drone_status = get_drone_status()
    battery_level = get_battery_level()
    flight_time = get_flight_time()
    altitude = get_temp()

    # Update the labels with the new data
    status_label.config(text=drone_status)
    battery_label.config(text=battery_level)
    flight_time_label.config(text=flight_time)
    altitude_label.config(text=altitude)

    # Schedule the function to be called again after 1000 milliseconds (1 second)
    root.after(1000, update_labels)

def main():
    global root, status_label, battery_label, flight_time_label, altitude_label
    
    root = tk.Tk()
    root.title("TELLO DRONE CONTROL PANEL")

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window size to 80% of screen width and height
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)

    # Set the geometry of the main window
    root.geometry(f"{window_width}x{window_height}")

    # Set the background color of the main window to dark gray
    root.configure(bg="darkgray")

    # Create a frame that takes 60% of the main window height and 100% of its width
    inner_frame_height = int(window_height * 0.6)

    inner_frame = tk.Frame(root, width=window_width, height=inner_frame_height, bg="gray")
    inner_frame.place(x=0, y=0)  # Place at the top of the window

    # Initialize labels
    status_label = tk.Label(inner_frame, text="", bg="gray", fg="white")
    status_label.pack(pady=10)

    battery_label = tk.Label(inner_frame, text="", bg="gray", fg="white")
    battery_label.pack(pady=10)

    flight_time_label = tk.Label(inner_frame, text="", bg="gray", fg="white")
    flight_time_label.pack(pady=10)

    altitude_label = tk.Label(inner_frame, text="", bg="gray", fg="white")
    altitude_label.pack(pady=10)

    # Start the update loop
    update_labels()

    root.mainloop()

if __name__ == "__main__":
    main()
