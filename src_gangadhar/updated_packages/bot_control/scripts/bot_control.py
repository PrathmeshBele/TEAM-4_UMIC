#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('bot_control', anonymous=True)
    


if __name__ == '__main__':
    try:
    	gripper(1)
    	front()
    	gripper(-1)
    	back()
    	

    except rospy.ROSInterruptException:
        pass
