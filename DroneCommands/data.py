from djitellopy import Tello

# Create a single Tello object and connect once
tello = Tello()
tello.connect()

def get_drone_status():
    # Fetch drone status
    return tello.get_current_state()

def get_battery_level():
    # Fetch battery level
    return tello.get_battery()

def get_flight_time():
    # Fetch flight time
    return tello.get_flight_time()

def get_temp():
    # Fetch highest temperature
    return tello.get_highest_temperature()
