import cv2
import numpy as np

def runCam(cam):
    while True:
        ret, frame = cam.read()
        cv2.imshow('webcam', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
runCam(cap)