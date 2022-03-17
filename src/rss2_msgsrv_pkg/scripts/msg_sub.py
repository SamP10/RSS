#! /usr/bin/env python

import rospy
from rss2_msgsrv_pkg.msg import date_cmd_vel

def callback(msg):
	rospy.loginfo(msg.sp_date)
	rospy.loginfo(msg.sp_cmd_vel)
	

rospy.init_node('msg_sub')
sub = rospy.Subscriber('/sp_topic', date_cmd_vel, callback)



rospy.spin()
