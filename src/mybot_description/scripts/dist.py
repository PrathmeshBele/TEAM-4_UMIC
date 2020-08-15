#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan

def callback(msg):
    print(msg.ranges)

rospy.init_node('scan_values')
sub = rospy.Subscriber('/mybot/laser/scan', LaserScan, callback)
rospy.spin()
