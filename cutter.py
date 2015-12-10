#!/usr/bin/python
#Author: Chris Corbett <ccc395@vt.edu>

#imports
import rospy
from sensor_msgs.msg import Vlt
from std_msgs.msg import String
import Adafruit_BBIO.ADC as ADC
import math

#setting up pin
ADC.setup()

def callback(event):
	voltage = ADC.read("P9_37")
	
	#minimum range
	if voltage > "number":
	  #stop
	else:
		#keep going
	else:

	#assign values and publish
	pub = rospy.Publisher('/voltage', Vlt, queue_size=10)
	rangeout = Vlt()
	rangeout.range = rangevalue
	rospy.loginfo(rangeout)
	pub.publish(rangeout)
	

#main function reads voltage and publishes Vlt value
#ranges reported in cm
def rangefunc():
	rospy.init_node('rangefunc', anonymous=True)

	rospy.Timer(rospy.Duration(1), callback)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		rangefunc()
	except rospy.ROSInterruptException:
		pass

    Status API Training Shop Blog About Pricing 

    © 2015 GitHub, Inc. Terms Privacy Security Contact Help 

