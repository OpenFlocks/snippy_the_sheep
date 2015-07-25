#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
motor_1_speed_pin = 13
motor_1_direction_pin = 15
motor_2_speed_pin = 16
motor_2_direction_pin = 18

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
