#! /usr/bin/env python

import rospy
from rss2_msgsrv_pkg.srv import srv_turtlebot_move, srv_turtlebot_moveResponse
from geometry_msgs.msg import Twist

def callback(request):
	rospy.loginfo('Turtlebot_move_service has been called')
	total_time = 0
	while total_time <= request.duration:
		total_time += 1
		if total_time <= 20:
			vel.linear.x = 0.2
			vel.angular.z = 0.2
		elif 20 < total_time  <=25:
			vel.linear.x = 0
			vel.angular.z = 0
		elif 25 < total_time <= 30:
			vel.linear.x = 0.2
		sp_pub.publish(vel)
		rospy.loginfo('time = %d',total_time)
		rate.sleep()
		total_time += 1
	vel.linear.x= 0.0
	vel.angular.z = 0.0
	sp_pub.publish(vel)
	rate.sleep()
	
	return srv_turtlebot_moveResponse(True)

rospy.init_node('turtlebot_move_server')

sp_service = rospy.Service('/turtlebot_move_service', srv_turtlebot_move, callback)

sp_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel=Twist()

rate = rospy.Rate(1)

rospy.loginfo('Service /turtlebot_move_service is ready!')

rospy.spin()
