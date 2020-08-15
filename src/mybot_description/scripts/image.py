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


def show_image(img):
    cv2.imwrite('/home/prathmesh/umic/src/mybot_description/scripts/lol.jpg',img)
    img=cv2.imread('/home/prathmesh/umic/src/mybot_description/scripts/lol.jpg')
    plt.imshow(img)
   
    cv2.waitKey(0)

 
def image_callback(img_msg):
    # 
    rospy.loginfo(img_msg.header)
    
    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
        #show_image(cv_image)
        cv2.imwrite('/home/prathmesh/umic/src/mybot_description/scripts/lol.jpg',cv_image)
        img=cv2.imread('/home/prathmesh/umic/src/mybot_description/scripts/lol.jpg')
        cv2.imshow('',img)
   
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
