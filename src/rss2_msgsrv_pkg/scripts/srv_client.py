#! /usr/bin/env python

import rospy

from gazebo_msgs.srv import GetLinkState, GetLinkStateRequest

rospy.init_node('service_client')

rospy.wait_for_service('/gazebo/get_link_sate')

get_pos_service = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)

get_pos_object = GetLinkStateRequest()

get_pos_object.link_name = 'turtlebot3_burger::base_footprint'
get_pos_object.reference_frame=''

result = get_pos_service(get_pos_object)

print(result)
