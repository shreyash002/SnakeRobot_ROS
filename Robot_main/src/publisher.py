#!/usr/bin/python
import rospy
from std_msgs.msg import Float64
import math
from math import sin,cos,atan2,sqrt,fabs

def joint_positions_publisher():

	#Initiate node for controlling joints positions.
	rospy.init_node('joint_positions_node', anonymous=True)

	#Define publishers for each joint position controller commands.
	pub1 = rospy.Publisher('/model8/joint1_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/model8/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/model8/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/model8/joint4_position_controller/command', Float64, queue_size=10)
	pub5 = rospy.Publisher('/model8/joint5_position_controller/command', Float64, queue_size=10)
	pub6 = rospy.Publisher('/model8/joint6_position_controller/command', Float64, queue_size=10)
	pub7 = rospy.Publisher('/model8/joint7_position_controller/command', Float64, queue_size=10)
	pub8 = rospy.Publisher('/model8/joint8_position_controller/command', Float64, queue_size=10)
	pub9 = rospy.Publisher('/model8/joint9_position_controller/command', Float64, queue_size=10)
	pub10 = rospy.Publisher('/model8/joint10_position_controller/command', Float64, queue_size=10)

	rate = rospy.Rate(100) #100 Hz

	#Define parameters
	a = 1
	b = 0.5
	w = 2

	#While loop to have joints follow a certain position, while rospy is not shutdown.
	i = 0
	while not rospy.is_shutdown():

		angle = (w*i)

		#Publish the same sine movement to each joint.
		pub1.publish(a*sin(angle))
		pub2.publish(a*sin(angle+b))
		pub3.publish(a*sin(angle+2*b))
		pub4.publish(a*sin(angle+3*b))
		pub5.publish(a*sin(angle+4*b))
		pub6.publish(a*sin(angle+5*b))
		pub7.publish(a*sin(angle+6*b))
		pub8.publish(a*sin(angle+7*b))
		pub9.publish(a*sin(angle+8*b))
		pub10.publish(a*sin(angle+9*b))

		i = i+1 #increment i

		rate.sleep() #sleep for rest of rospy.Rate(100)

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
	try: joint_positions_publisher()
	except rospy.ROSInterruptException: pass
