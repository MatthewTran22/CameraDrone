from djitellopy import tello 
import cv2
import threading


camdroid = tello.Tello()
active = True

camdroid.connect()
camdroid.takeoff()
camdroid.streamoff()
camdroid.streamon()

def reposition():
    #Idle movement
    camdroid.move_up(20)
    camdroid.move_down(20)
    #TODO: recieve flags to move left right up down from method getFacePosition

while active:
    print(camdroid.get_battery())
    threading.Thread(target=reposition).start()
    #Needs to be threaded, bop up and down to not trigger auto land, and constantly recieve frame data
    #Probably make the bob up and down for hover method in drone reposition code
    # Thread call  threading.Thread(target = run, daemon = True).start()
    frame = camdroid.get_frame_read()
    currFrame = frame.frame
    img = cv2.resize(currFrame, (900,600))
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Changes the blue coloring back to yellow AKA code is racist
    cv2.imshow("Drone View", img)
    if cv2.waitKey(1) == ord('q'):
        active = False

print(camdroid.get_battery())
camdroid.land()

camdroid.streamoff()
cv2.destroyAllWindows()