import cv2

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/harrcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.2,8)

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow("Test", img)
    cv2.waitKey(1)