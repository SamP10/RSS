#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


def position(msg):
	global x
	global y
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	if x <3:
		print("X: ", x)
	elif x > 3:
		move.linear.x = 0
		


rospy.init_node('odom_pubsub')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate=rospy.Rate(10)
move=Twist()

rate.sleep()
		
sub = rospy.Subscriber('/odom', Odometry, position)
move.linear.x = 0.5
#	move.linear.x =0

while not rospy.is_shutdown():
	pub.publish(move)

