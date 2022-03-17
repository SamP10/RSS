#! /usr/bin/env python

from __future__ import print_function
import rospy

from std_srvs.srv import SetBool, SetBoolResponse

def pw_callback(request):
	rospy.loginfo("Setbool Server has been called")
	cur_response = SetBoolResponse()
	if request.data == True:
		cur_response.success = True
		cur_response.message = 'OK'
		return cur_response
	else:
		cur_response.success = False
		cur_response.message = 'Not OK'
		return cur_response

rospy.init_node('pw_srv_server')

pw_service = rospy.Service('setBool_service', SetBool, pw_callback)
rospy.loginfo('Service /setBool_service is ready!')

rospy.spin()
