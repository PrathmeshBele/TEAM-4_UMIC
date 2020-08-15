import cv2
from matplotlib import pyplot as plt
import numpy as np

left_cascade = cv2.CascadeClassifier('left_cascade.xml')
right_cascade = cv2.CascadeClassifier('right_cascade.xml')

test_imgs = ['test1.jpeg', 'test2.jpeg', 'test3.jpeg', 'test4.jpeg', 'test5.jpeg', 'left.jpg', 'right.jpg']

for case in test_imgs:
    img = cv2.imread(case, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    left = left_cascade.detectMultiScale(gray, 1.5, 3)
    right = right_cascade.detectMultiScale(gray, 1.5, 3)

    if (left == ()) and (right == ()):
        #continue straight
        pass
    else:
        if left == ():
            print("go right")
            for (x,y,w,h) in right:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #code for going right
        else:
            print("go left")
            for (x,y,w,h) in left:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #code for going left

    cv2.imshow('img', img)
    cv2.waitKey(0)

cv2.DestroyAllWindows()
