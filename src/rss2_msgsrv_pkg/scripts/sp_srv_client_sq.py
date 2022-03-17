#! /usr/bin/env python

import rospy

from  rss2_msgsrv_pkg.srv import turtlebot_move_square, turtlebot_move_squareRequest

rospy.init_node('turtlebot_square_client')

rospy.wait_for_service('/turtlebot_square_service')

turtlebot_service_client = rospy.ServiceProxy('/turtlebot_square_service', turtlebot_move_square)

turtlebot_request_instance = turtlebot_move_squareRequest()
turtlebot_request_instance.sideLength = 4
turtlebot_request_instance.repetitions = 2

feedback = turtlebot_service_client(turtlebot_request_instance)

rospy.loginfo(str(feedback))
rospy.loginfo('End of service call')
