#!/usr/bin/python

import rospy
from std_msgs.msg import String
from time import sleep

# Publish
def think(action):
    pub = rospy.Publisher('thought_topic', String, queue_size=10)

    r = rospy.Rate(10) # 10hz

    rospy.loginfo(action)
    pub.publish(action)

def move(direction):
    pub = rospy.Publisher('direction_topic', String, queue_size=10)

    r = rospy.Rate(10) # 10hz

    rospy.loginfo(direction)
    pub.publish(direction)

# Subscribe
def callback(data):
    rospy.loginfo(rospy.get_caller_id()+": %s",data.data)

def listen():
    rospy.Subscriber("thought_topic", String, callback)

def callback_drive_status(data):
    rospy.loginfo(rospy.get_caller_id()+": %s",data.data)

def drive_status():
    rospy.Subscriber("status_topic", String, callback_drive_status)

if __name__ == '__main__':
    print "starting brain"
    try:
        rospy.init_node('brain', anonymous=True)

        print "calling listen()"
        listen()

        print "calling think()"
        think('I am awake')

        # weird ros glitch, fixed by calling stop before publishing subsequent commands to direction_topic
        print "calling move(stop)"
        move('stop')
        sleep(5)

        print "calling move(foward)"
        move('forward')
        sleep(5)

        print "calling move(stop)"
        move('stop')
        sleep(5)

        print "calling move(reverse)"
        move('reverse')
        sleep(5)

        print "calling move(stop)"
        move('stop')

        rospy.spin()

    except rospy.ROSInterruptException: pass