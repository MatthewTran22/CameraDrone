from djitellopy import tello
import cv2

camdroid = tello.Tello()

camdroid.connect()
camdroid.streamoff()
camdroid.streamon()

while True:
    frame = camdroid.get_frame_read()
    currFrame = frame.frame
    img = cv2.resize(currFrame, (600,600))
    cv2.imshow("Drone View", img)
    if cv2.waitKey(1) == ord('q'):
        break
print(camdroid.get_battery())

camdroid.land()
camdroid.streamoff()
cv2.destroyAllWindows()