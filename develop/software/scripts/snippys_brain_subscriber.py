#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard snippy think something: %s",data.data)
    
def listener():
    rospy.init_node('snippys_brain_subscriber', anonymous=True)

    rospy.Subscriber("thought_pub_topic", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
