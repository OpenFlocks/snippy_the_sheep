#!/usr/bin/python
import ConfigParser
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

cfg = ConfigParser.ConfigParser()
cfg.read("../config-rpi-1-model-b.ini")
motor_1_speed_pin = cfg.get('motor_pins', 'motor_1_speed_pin')
motor_1_direction_pin = cfg.get('motor_pins', 'motor_1_direction_pin')
motor_2_speed_pin = cfg.get('motor_pins', 'motor_2_speed_pin')
motor_2_direction_pin = cfg.get('motor_pins', 'motor_2_direction_pin')

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

def stop():
	GPIO.output(motor_1_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
	GPIO.output(motor_1_speed_pin, 0) # 0 == stop, 255 == fastest.
	GPIO.output(motor_2_direction_pin, GPIO.LOW) # 0 == fwd, 1 == rev.
	GPIO.output(motor_2_speed_pin, 0) # 0 == stop, 255 == fastest.	

while True:
	cmd = raw_input("Enter f (forward) or r (reverse) or s (stop): ")
	direction = cmd[0]
	if direction == "f":
		forward()
	if direction == "r":
		reverse()
	if direction == "s":
		stop()

GPIO.cleanup()
