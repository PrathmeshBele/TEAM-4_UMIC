import cv2
from matplotlib import pyplot as plt
import numpy as np

left_cascade = cv2.CascadeClassifier('left_cascade.xml')
right_cascade = cv2.CascadeClassifier('right_cascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    left = left_cascade.detectMultiScale(gray)
    right = right_cascade.detectMultiScale(gray)

    if len(right)>0:
        print("go right")
        x,y,w,h=right[0]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #code for going right
    elif len(left)>0:
        print("go left")
        x,y,w,h=left[0]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #code for going left

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
DestroyAllWindows()
