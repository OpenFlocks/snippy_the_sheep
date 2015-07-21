# doctest Raspberry Pi GPIO Module

Test the RPi.GPIO and your **[RPi B board rev2](https://raspberrypiwonderland.files.wordpress.com/2014/02/raspberry-pi-rev2-gpio-pinout.jpg)** setup by running this markdown file through doctest:

	pi@raspberrypi~/scripts $ sudo python -m doctest -v test_rpi_gpio_setup.md﻿

1. ## Import sleep to pause tests for n seconds.
	```
	>>> from time import sleep
	>>> 

	```

1. ## Test you have RPi.GPIO installed
	```
	>>> import RPi.GPIO as GPIO
	>>> 

	```

1. ## RPi Board Info + RPi.GPIO Version
	* To discover the Raspberry Pi board revision:
		```
		>>> GPIO.RPI_INFO['P1_REVISION']
		2

		```
		* To discover the version of RPi.GPIO:
		```
		>>> GPIO.VERSION
		'0.5.11'

		```
	
1. ## Pin Numbering GPIO mode
	* GPIO.BOARD == 10
		* Use this one.
	* GPIO.BCM == 11
		* Don't use this one.
		```
		>>> GPIO.setmode(GPIO.BOARD)
		>>>

		```
	
1. ## Warnings Spam Off
	```	
	>>> GPIO.setwarnings(False)
	>>>

	```

1. ## Setup Your Channels
	* You need to setup every channel you are using as an input or an output.
	* You can also specify an initial value for your output channel:
		```
		GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
		```
	* e.g. wire your GPIO connection to your dual motor controller.
		```
		TO DO: chan_list_input = [9,10]
		GPIO.setup(chan_list_input, GPIO.IN)
		``` 
		```
		>>> chan_list_output = [7] # Pin 7 == GPIO4
		>>> GPIO.setup(chan_list_output, GPIO.OUT)
		>>> 
	
		```
1. ## Output
	* Set the output state of a GPIO pin
	* State can be either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
	* e.g. confirm you can control the direction of the 2 motors attached to the motor controller.
		```
		>>> chan_list_output = [7] # Pin 7 == GPIO4
		>>> GPIO.output(chan_list_output, GPIO.HIGH) # Sets all to 1 / True. LED on.
		>>> sleep(3)
		>>> GPIO.output(chan_list_output, GPIO.LOW) # Sets all to 0 / False. LED off.
		>>> GPIO.cleanup()
		>>>

		```
	* Note: this sets 1st to low, 2nd to high:
	
		```GPIO.output(chan_list_output, GPIO.LOW, GPIO.HIGH)```

1. ## RPi.GPIO.PWM
	1. An example to blink an LED once every two seconds.
		* Note: I have removed this doctest as 'Press return' will incorrectly trigger a  test failure (a 'false positive').
		```
		 import RPi.GPIO as GPIO
		 GPIO.setmode(GPIO.BOARD)
		 GPIO.setup(7, GPIO.OUT)

		 p = GPIO.PWM(7, 0.5)
		 p.start(1)
		 raw_input('Press return to stop') # use raw_input for Python 2. raw for Python 3
		 p.stop()
		 GPIO.cleanup()


		```

	1. An example to brighten/dim an LED:
		```
		>>> import time
		>>> import RPi.GPIO as GPIO
		>>> GPIO.setmode(GPIO.BOARD)
		>>> GPIO.setup(7, GPIO.OUT)

		>>> p = GPIO.PWM(7, 50)  # channel=7 frequency=50Hz
		>>> p.start(0)
		>>> try:
		... 	while 1:
		... 		for dc in range(0, 101, 5):
		... 			p.ChangeDutyCycle(dc)
		... 			time.sleep(0.1)
		... 		for dc in range(100, -1, -5):
		... 			p.ChangeDutyCycle(dc)
		... 			time.sleep(0.1)
		... except KeyboardInterrupt:
		... 	pass
		>>> p.stop()
		>>> GPIO.cleanup()
		>>>

		```

1. ## Input - TO DO
	* Read the value of a GPIO pin
	* This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
	* e.g. confirm you can read the input pins from the motor controller.
		```
		chan_list_input = [9,10]
		GPIO.input(chan_list_input[0]) # Reading input channel 9, test if it returns "GPIO.LOW".
		GPIO.LOW
		
		```
	
1. ## Cleanup - TO DO
	Returning all channels you have used back to inputs with no pull up/down to avoid accidental damage to your RPi by shorting out the pins.
	```
	>>> GPIO.cleanup()
	>>>

	```