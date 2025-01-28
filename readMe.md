# CameraDrone

## Overview
This project utilizes the DJI Tello Drone to keep the user's face in the center of its camera

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CameraDrone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CameraDrone/DroneCommands
    ```
3. Activate the virtual environment:
    ```bash
    #For Windows
    source venvWin/Scripts/activate
    #For Mac
    source venvMac/bin/activate 
    ```

## Usage
1. Connect the drone to your computer.
2. Start the application:
    ```bash
    python facetrack.py
    ```
3. On takeoff, raise the drone to head level by placing your hand under the drone's bottom sensors
4. Once at the desired height, stand in front of the camera and let the software do the rest
5. Deactivate the software by pressing CTRL+C in the terminal

## How it works
The program utilizes the drone's camera to return its video feed to the software. OpenCV then utilizes its [frontal face haar cascade file](https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) to return the coordinates of the detected face within the image. The absolute center is also determined based on the resolution size of the image and the face dimensions. Once both are compared, the DJI Tello library will increase speed in the X or Y direction to reduce the difference between the two areas.
