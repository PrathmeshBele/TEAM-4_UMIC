#!/usr/bin/env python
 

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import numpy as np
from math import atan2,asin
from std_msgs.msg import String
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
 
i=0

def calculate_lines(frame, lines):
    # Empty arrays to store the coordinates of the left and right lines
    left = []
    right = []
    # Loops through every detected line
    for line in lines:
        # Reshapes line from 2D array to 1D array
        x1, y1, x2, y2 = line.reshape(4)
        # Fits a linear polynomial to the x and y coordinates and returns a vector of coefficients which describe the slope and y-intercept
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        y_intercept = parameters[1]
        # If slope is negative, the line is to the left of the lane, and otherwise, the line is to the right of the lane
        #if slope < 0:
           # left.append((slope, y_intercept))
        #else:
            #right.append((slope, y_intercept))
        left.append((slope,y_intercept))
    # Averages out all the values for left and right into a single slope and y-intercept value for each line
    left_avg = np.average(left, axis = 0)
    #right_avg = np.average(right, axis = 0)
    # Calculates the x1, y1, x2, y2 coordinates for the left and right lines
    left_line = calculate_coordinates(frame, left_avg)
    #right_line = calculate_coordinates(frame, right_avg)
    return np.array([left_line])

def calculate_coordinates(frame, parameters):
    slope, intercept = parameters
    # Sets initial y-coordinate as height from top down (bottom of the frame)
    y1 = frame.shape[0]
    # Sets final y-coordinate as 150 above the bottom of the frame
    y2 = int(y1 -200)#- 150)
    # Sets initial x-coordinate as (y1 - b) / m since y1 = mx1 + b
    x1 = int((y1 - intercept) / slope)
    # Sets final x-coordinate as (y2 - b) / m since y2 = mx2 + b
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])
def visualize_lines(frame, lines):
    # Creates an image filled with zero intensities with the same dimensions as the frame
    lines_visualize = np.zeros_like(frame)
    # Checks if any lines are detected
    if lines is not None:
        #m=np.zeros(4)
        for x1, y1, x2, y2 in lines:
            #m=[x1,y1,x2,y2]+m
            # Draws lines between two coordinates with green color and 5 thickness
            cv2.line(lines_visualize, (x1, y1), (x2, y2), (0, 255, 0), 5)
            
        #m=m/2
        #cv2.line(lines_visualize, (int(m[0]), int(m[1])), (int(m[2]), int(m[3])), (0, 255, 255), 5)

    return lines_visualize


def show_image(img):
    cv2.imwrite('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg',img)
    img=cv2.imread('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg')
    plt.imshow(img)
   
    cv2.waitKey(0)

 
def image_callback(img_msg):
    # 
    rospy.loginfo(img_msg.header)
    
    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
        #show_image(cv_image)
        cv2.imwrite('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg',cv_image)
        img=cv2.imread('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg')
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (400, 400))  
        color_boundaries = [ # colors can be changed
	#([17, 15, 100], [90, 96, 255]), #red
	#([20, 90, 4], [90, 255, 100]), #green
	([50, 79, 83], [80, 140, 140]) ]# yellow]
        
        for (lower,upper) in color_boundaries:

            lower=np.array(lower,dtype='uint8')
            upper=np.array(upper,dtype='uint8')
            mask=cv2.inRange(img,lower,upper)
            output=cv2.bitwise_and(img,img,mask=mask)
            
           
        
        segment=output #+masks[1]+masks[2]
        gray=cv2.cvtColor(segment,cv2.COLOR_BGR2GRAY)
        kernel = np.ones((7,7), np.uint)
        gray=cv2.dilate(gray, kernel, iterations=1) 
        ret,thresh1 = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
        lane = cv2.Canny(thresh1,90,170)
        hough = cv2.HoughLinesP(lane, 1, np.pi / 180, 80, np.array([]), minLineLength = 5, maxLineGap = 50)
        try:
             
            lines = calculate_lines(img, hough)
        #lines_visualize = visualize_lines(img, lines)
            cv2.line(segment, (lines[0][0], lines[0][1]), (lines[0][2], lines[0][3]), (0, 255, 0), 3)
            cv2.imshow('',segment) 
        except:
            cv2.imshow('',segment)


        cv2.waitKey(100)   
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))
   
def listener():
    
 
    rospy.init_node('opencv_example', anonymous=False)

    rospy.Subscriber("/mybot/camera1/image_raw", Image, image_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

 
 
if __name__ == '__main__':
    listener()
 
#cv2.namedWindow("Image Window", 1)

 
 # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
#while not rospy.is_shutdown():
    
  #  rospy.spin()
