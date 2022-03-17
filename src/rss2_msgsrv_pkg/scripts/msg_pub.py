#! /usr/bin/env python

import rospy
from rss2_msgsrv_pkg.msg import date_cmd_vel
from geometry_msgs.msg import Twist

from datetime import datetime

rospy.init_node('msg_pub')

now = datetime.now()
date_str = now.strftime("%m/%d/%y, %H:%M:%S")

sp_cmd_vel = date_cmd_vel()
sp_cmd_vel.sp_date = date_str
sp_cmd_vel.sp_cmd_vel.linear.x = 0.5
sp_cmd_vel.sp_cmd_vel.angular.z = 0.1

pub = rospy.Publisher('/sp_topic', date_cmd_vel, queue_size=1)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
	pub.publish(sp_cmd_vel)
	rate.sleep()
