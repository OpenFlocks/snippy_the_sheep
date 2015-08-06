#!/usr/bin/python

import rospy
from std_msgs.msg import String
#import drive

# Publisher
def think(action):
    pub = rospy.Publisher('thought_topic', String, queue_size=10)

    r = rospy.Rate(10) # 10hz

    str = action
    # print str
    rospy.loginfo(str)
    pub.publish(str)

# Subscriber
def callback(data):
    rospy.loginfo(rospy.get_caller_id()+": %s",data.data)

def listen():
    rospy.Subscriber("thought_topic", String, callback)

if __name__ == '__main__':
    print "starting brain"
    try:
        rospy.init_node('brain', anonymous=True)

        print "calling listen()"
        listen()

        print "calling think()"
        think('I am awake')

        rospy.spin()

    except rospy.ROSInterruptException: pass