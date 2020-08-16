import cv2
from matplotlib import pyplot as plt
import numpy as np

color_boundaries = [ # colors can be changed
	#([17, 15, 100], [90, 96, 255]), #red
	#([20, 90, 4], [90, 255, 100]), #green
	([0, 90, 90], [20, 120, 120]) # yellow
]
min_area = 5 #toggle-able value
darkness = 60 #toggle-able value

def is_arrow(cnt):
    epsilon = 0.012*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    if(len(approx)<7):
        pass
    else:
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        approx = np.array(approx)
        approx_x = approx[:, 0, 0]      #all x coordinates of the contour points
        mask1 = approx_x > cx
        mask2 = approx_x < cx
        test = len(approx_x[mask1])-len(approx_x[mask2])
        if(test<=2 and test>=-2):
            pass
        elif(test>2):
            turn_right(cnt)
        else:
            turn_left(cnt)

def turn_left(cnt):
    if(cv2.contourArea(cnt)>min_area):
        #rostopic to turn left
        print("going left")
    else:
        pass

def turn_right(cnt):
    if(cv2.contourArea(cnt)>min_area):
    #rostopic to turn right
        print("going right")
    else:
        pass

test_imgs = ['test1.jpeg', 'test2.jpeg', 'test3.jpeg', 'test4.jpeg', 'test5.jpeg', 'left.jpg', 'right.jpg']

for case in test_imgs:
    img = cv2.imread(case, 1)
    img = cv2.resize(img, (400, 350))

    masks=[]
    for (lower,upper) in color_boundaries:
        lower=np.array(lower,dtype='uint8')
        upper=np.array(upper,dtype='uint8')
        mask=cv2.inRange(img,lower,upper)

        output=cv2.bitwise_and(img,img,mask=mask)
        masks.append(output)

    segment=masks[0]
    cv2.imshow("check", segment)
    cv2.waitKey(0)
    gray=cv2.cvtColor(segment,cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, darkness, 255, 0)
    cv2.imshow("check", thresh)
    cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        is_arrow(cnt)
