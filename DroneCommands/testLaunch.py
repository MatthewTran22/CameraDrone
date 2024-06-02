from djitellopy import tello 
import cv2

camdroid = tello.Tello()

camdroid.connect()
camdroid.takeoff()
camdroid.streamoff()
camdroid.streamon()

while True:
    print(camdroid.get_battery())
    camdroid.move_up(20)
    camdroid.move_down(20)
    #Needs to be threaded, bop up and down to not trigger auto land, and constantly recieve frame data
    #Probably make the bob up and down for hover method in drone reposition code
    frame = camdroid.get_frame_read()
    currFrame = frame.frame
    img = cv2.resize(currFrame, (600,600))
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Changes the blue coloring back to yellow AKA code is racist
    cv2.imshow("Drone View", img)
    if cv2.waitKey(1) == ord('q'):
        camdroid.land()
        break

print(camdroid.get_battery())

camdroid.streamoff()
cv2.destroyAllWindows()