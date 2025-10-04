import cv2
import os

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 720)

while True:
    success, img = cap.read()
    cv2.imshow("Face Attendance", img)
    cv2.waitKey(1)