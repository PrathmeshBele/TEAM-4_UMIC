#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('controller', anonymous=True)
    
def horizontal(x):
    pub = rospy.Publisher('/claw_horizontal_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    temp = x - 0.1
    while temp < x:
        position = temp
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        temp = temp + 0.01

def vertical(z):
    pub = rospy.Publisher('/claw_vertical_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    temp = z - 0.1
    while temp < z:
        position = temp
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        temp = temp + 0.01

def gripper(theta):
    pub = rospy.Publisher('/claw_gripper_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(30) # 10hz
    temp = theta - 1
    while temp < theta:
        angle = temp
        rospy.loginfo(angle)
        pub.publish(angle)
        rate.sleep()
        temp = temp + 0.1

if __name__ == '__main__':
    try:
    	
    	
    	gripper(1.05)
    	vertical(-0.1)
    	
    	
    	
    	gripper(0)
    	vertical(0.1)
        horizontal(-0.1)
        
    except rospy.ROSInterruptException:
        pass
