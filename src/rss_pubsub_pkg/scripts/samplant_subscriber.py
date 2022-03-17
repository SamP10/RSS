#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

def callback(msg):
	print('Linear velocity is')
	print(msg.linear)
	print('Angular velocity is')
	print(msg.angular)

rospy.init_node('samplant_subscriber')
sub = rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)

rospy.spin()
