from djitellopy import tello 
import cv2
import threading
import time


camdroid = tello.Tello()
active = True
def hover():
    camdroid.rotate_clockwise(1)
    time.sleep(500)
    camdroid.rotate_counter_clockwise(1)


    
camdroid.connect()
camdroid.takeoff()
camdroid.streamoff()
camdroid.streamon()


while active:
    print(camdroid.get_battery())
    threading.Thread(target = hover).start()
    #Needs to be threaded, bop up and down to not trigger auto land, and constantly recieve frame data
    #Probably make the bob up and down for hover method in drone reposition code
    # Thread call  threading.Thread(target = run, daemon = True).start()
    frame = camdroid.get_frame_read()
    currFrame = frame.frame
    img = cv2.resize(currFrame, (900,600))
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Changes the blue coloring back to yellow AKA code is racist
    cv2.imshow("Drone View", img)
    if cv2.waitKey(1) == ord('q'):
        camdroid.streamoff()
        cv2.destroyAllWindows()
        active = False

print(camdroid.get_battery())
camdroid.land()

