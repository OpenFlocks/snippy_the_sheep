#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def thinker():
    rospy.init_node('snippys_brain_publisher', anonymous=True)
    
    pub = rospy.Publisher('thought_pub_topic', String, queue_size=10)

    r = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        str = "Hello snippy!, he thought to himself. %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    try:
        thinker()
    except rospy.ROSInterruptException: pass
