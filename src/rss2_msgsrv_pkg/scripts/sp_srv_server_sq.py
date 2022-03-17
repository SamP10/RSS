#! /usr/bin/env python

import rospy
from rss2_msgsrv_pkg.srv import turtlebot_move_square, turtlebot_move_squareResponse
from geometry_msgs.msg import Twist

def callback(request):
	rospy.loginfo('Turtlebot_square_service has been called')
	repetitions = request.repetitions
	length = request.sideLength
	time = length / 0.5
	for r in range(repetitions):
		time_count = 0
		square(time)
		print"Square ", r+1		
	vel.linear.x = 0.0
	vel.angular.z = 0.0
	sp_pub.publish(vel)
	rate.sleep()
	return turtlebot_move_squareResponse(True)

def square(time):
    s = 0
    for s in range(3):
	time_count=0
	rospy.sleep(1)
	while time_count <= time:
		if time_count < time:
       			forward()
		#elif time_count == time-1:
    		#	stop()
		else:
			stop()
			turn()
			rospy.sleep(1)
			stop()
			print(vel)
			rospy.sleep(1)

		time_count += 1
	s+=1
    rate.sleep()

def stop():
	print("Stop")
	vel.linear.x = 0
	vel.linear.y = 0
	vel.angular.z = 0.00000000000000000000
	sp_pub.publish(vel)
	rospy.sleep(1.5)


def turn():
	print("Turn")
	vel.linear.x = 0
	vel.angular.z = 1.5708
	sp_pub.publish(vel)

def forward():
	print("Forward")
	print(vel)
	vel.linear.x = 0.5
	vel.linear.y = 0.5
	vel.angular.z = 0.000000000000
	sp_pub.publish(vel)
	rate.sleep()

rospy.init_node('turtlebot_square_server')
sp_service = rospy.Service('/turtlebot_square_service', turtlebot_move_square, callback)
sp_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel=Twist()
rate=rospy.Rate(1)
rospy.loginfo('Service /turtlebot_square_service is ready!')
rospy.spin()
