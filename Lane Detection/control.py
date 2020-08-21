#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic
import rospy
import numpy as np
from math import atan2,asin
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
import time
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
msg=Twist()
def controls(cx,cy):
    error=cx-200
    msg.angular.z=-(error/10)#-integral_sum/300
    msg.linear.x=0.1#-abs(error/2000)
    pub.publish(msg)
i=0
def stop_controls(rx,ry):
    time.sleep(0.1)
    error_stop=150-ry
    msg.linear.x=0
    msg.angular.z=0
    pub.publish(msg)
    time.sleep(0.1)
    msg.linear.x=0
    msg.angular.z=-100
    pub.publish(msg)
    time.sleep(0.3)
  

def centroid_callback(array_msg):
    array=array_msg.data
    #rospy.loginfo(array)
    #cx,cy,rx,ry=array[0],array[1],array[2],array[3]
    ## code for subscribing to arrow.py and define global variable for none,right and left
    if array[0]>190 and array[1]>390:
        stop_controls(array[2],array[3])

    else:
        controls(array[0],array[1])

 
   
def listener():
    
 
    rospy.init_node('bot_controls', anonymous=False)
 
    rospy.Subscriber('centroid_info',Int32MultiArray, centroid_callback)
    #rospy.Subscriber("/arrow_msg", String, arrow_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

 
if __name__ == '__main__':
    listener()
 
#cv2.namedWindow("Image Window", 1)
 # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
#while not rospy.is_shutdown():    
#  rospy.spin()
