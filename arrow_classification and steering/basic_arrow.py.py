import numpy as np
import cv2

min_area = 100 #toggle-able value
darkness = 127 #toggle-able value
k = 0.012 #toggle-able value

def is_arrow(cnt):
    epsilon = 0.012*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    if(len(approx)<7):
        go_straight()
    else:
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        approx = np.array(approx)
        approx_x = approx[:, 0, 0]      #all x coordinates of the contour points
        mask1 = approx_x > cx
        mask2 = approx_x < cx
        test = len(approx_x[mask1])-len(approx_x[mask2])
        if(test<=2 and test>=-2):
            go_straIght()
        elif(test>2):
            turn_right(cnt)
        else:
            turn_left(cnt)

def go_straight():
    # msg to go go_straight
    #mostly x=max value all others 0
    print("going straight")

def turn_left(cnt):
    if(cv2.contourArea(cnt)>min_area):
        #rostopic to turn left
        print("going left")
    else:
        go_straight()

def turn_right(cnt):
    if(cv2.contourArea(cnt)>min_area):
    #rostopic to turn right
        print("going right")
    else:
        go_straight()

imgs = ["left.jpg", "right.jpg"]

for k in imgs:
    im = cv2.imread(k)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,darkness,255,1)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        is_arrow(cnt)
