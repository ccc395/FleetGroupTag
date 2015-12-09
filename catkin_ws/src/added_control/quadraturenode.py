#!/usr/bin/env python
# node by Chris Corbett <ccc395@vt.edu>
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from khan_msgs.msg import Quadrature
import quadrature

quad = quadrature.QuadratureEstimator(1000)

def callback(data):
    #Takes data from bag file and runs through update function
    quad.update(data.state_a.data, data.state_b.data, data.header.stamp.to_sec())
    pub = rospy.Publisher('joint_out', JointState)
    #assigning values to JointState
    quadrature_out = JointState()
    quadrature_out.header.stamp = quad._time
    quadrature_out.position = quad._position
    quadrature_out.velocity = quad._velocity

    #Final publish of JointState
    rospy.loginfo(quadout)
    pub.publish(quadout)

def quadraturetalker():
    #subscribed to /ticks
    rospy.init_node('quadraturetalker', anonymous=True)
    rospy.Subscriber('/ticks', Quadrature, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        quadraturetalker()
    except rospy.ROSInterruptException:
        pass
