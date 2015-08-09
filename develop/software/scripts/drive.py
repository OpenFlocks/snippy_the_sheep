#!/usr/bin/python

import rospy
from std_msgs.msg import String
import ConfigParser
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

cfg = ConfigParser.ConfigParser()
cfg.read("../config_rpi_1_model_b.ini")
motor_1_speed_pin = int(cfg.get('motor_pins', 'motor_1_speed_pin'))
motor_1_direction_pin = int(cfg.get('motor_pins', 'motor_1_direction_pin'))
motor_2_speed_pin = int(cfg.get('motor_pins', 'motor_2_speed_pin'))
motor_2_direction_pin = int(cfg.get('motor_pins', 'motor_2_direction_pin'))

GPIO.setup(motor_1_speed_pin, GPIO.OUT)
GPIO.setup(motor_1_direction_pin, GPIO.OUT)
GPIO.setup(motor_2_speed_pin, GPIO.OUT)
GPIO.setup(motor_2_direction_pin, GPIO.OUT)

def forward():
    GPIO.output(motor_1_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
    GPIO.output(motor_1_speed_pin, 127) # 0 == stop, 255 == fastest.
    GPIO.output(motor_2_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
    GPIO.output(motor_2_speed_pin, 127) # 0 == stop, 255 == fastest.

def reverse():
    GPIO.output(motor_1_direction_pin, GPIO.HIGH) # 0 == fwd, 1 == rev.
    GPIO.output(motor_1_speed_pin, 127) # 0 == stop, 255 == fastest.
    GPIO.output(motor_2_direction_pin, GPIO.HIGH) # 0 == fwd, 1 == rev.
    GPIO.output(motor_2_speed_pin, 127) # 0 == stop, 255 == fastest.

# def forward(speed):
# 	TO DO
#
# def reverse(speed):
# 	TO DO
#
# def left(degrees):
# 	TO DO
#
# def right(degrees):
# 	TO DO

def stop():
    GPIO.output(motor_1_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
    GPIO.output(motor_1_speed_pin, 0) # 0 == stop, 255 == fastest.
    GPIO.output(motor_2_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
    GPIO.output(motor_2_speed_pin, 0) # 0 == stop, 255 == fastest.

# Publishers
def status(state):
    pub = rospy.Publisher("status_topic", String, queue_size=10)

    r = rospy.Rate(10) # 10hz

    rospy.loginfo(str(state))
    pub.publish(str(state))

# Subscribers
def callback(data): # callback for thought_topic
    if (len(data.data.split())) == 1:
        command = data.data.split()[0]

    rospy.loginfo(rospy.get_caller_id()+": %s",data.data)
    if command == 'forward':
        forward()
        status('driving foward')
    elif command == 'reverse':
        reverse()
        status('driving backward')
    elif command == 'stop':
        stop()
        status('stopped driving')

def listen():
    rospy.Subscriber("direction_topic", String, callback)

def callback_status(data): # callback for status_topic
    rospy.loginfo(rospy.get_caller_id()+": %s",data.data)

def listen_status():
    rospy.Subscriber("status_topic", String, callback_status)

if __name__ == '__main__':
    # When drive hears thought to move
    # then moves direction
    # and publishes status
    # for brain to receive
    print 'starting drive'
    try:
        rospy.init_node('drive', anonymous=True)

        print 'calling listen()'
        listen()

        rospy.spin()

    except rospy.ROSInterruptException: pass