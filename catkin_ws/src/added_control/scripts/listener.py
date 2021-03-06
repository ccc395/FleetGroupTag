#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def change(data):
    
    self._velocity = direction + vel
    position = velocity * time
    rospy.loginfo(rospy.get_caller_id() + "what I heard is %s", data.data)
    Header header
    std_msgs/Bool state_a
    std_msgs/Bool state_b

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/ticks", Bool, change)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

#!/usr/bin/env python
#import rospy
#from std_msgs.msg import String

#def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    
#def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
#    rospy.init_node('listener', anonymous=True)

#    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
#    rospy.spin()

#if __name__ == '__main__':
#    listener()
