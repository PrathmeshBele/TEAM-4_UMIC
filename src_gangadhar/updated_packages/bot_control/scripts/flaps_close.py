#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('flaps_control', anonymous=True)

pub_lf = rospy.Publisher('/bot1_lf_controller/command', Float64, queue_size=10)
pub_rf = rospy.Publisher('/bot1_rf_controller/command', Float64, queue_size=10)
rate = rospy.Rate(10)


def close_flaps():
	while not rospy.is_shutdown():
		pub_lf.publish(-30)
		pub_rf.publish(30)
		rate.sleep()
		
if __name__ == "__main__":
  try:
  	close_flaps()


  	
  except rospy.ROSInterruptException:
  	pass
