# doctest Raspberry Pi GPIO Module

Test the RPi.GPIO and your **[RPi B board rev2](https://raspberrypiwonderland.files.wordpress.com/2014/02/raspberry-pi-rev2-gpio-pinout.jpg)** setup by running this markdown file through doctest:

	pi@raspberrypi~/scripts $ python -m doctest -v test_rpi_gpio_setup.md﻿

1. ## RPi Board Info + RPi.GPIO Version
	* To discover information about your RPi:
		```
		GPIO.RPI_INFO
		```
	* To discover the Raspberry Pi board revision:
		```
		GPIO.RPI_INFO['P1_REVISION']
		```
	* To discover the version of RPi.GPIO:
		```
		GPIO.VERSION
		```

1. ## Test you have RPi.GPIO installed
	```
	>>> import RPi.GPIO as GPIO
	>>> 

	```
	
1. ## Pin Numbering GPIO mode
	* GPIO.BOARD == 10
	* GPIO.BCM == 11
		```
		GPIO.setmode(GPIO.BOARD)
		```
	
1. ## Warnings Spam Off
	```	
	GPIO.setwarnings(False)
	```

1. ## Setup Your Channels - TO DO
	* You need to setup every channel you are using as an input or an output.
	* You can also specify an initial value for your output channel:
		```
		GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
		```
	* e.g. wire your GPIO connection to your dual motor controller.
		```
		>>> chan_list_input = [9,10]
		>>> GPIO.setup(chan_list_input, GPIO.IN)
		>>> 
	
		>>> chan_list_output = [11,12]
		>>> GPIO.setup(chan_list_output, GPIO.OUT)
		>>> 
	
		```
1. ## Output - TO DO
	* Set the output state of a GPIO pin
	* State can be either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
	* e.g. confirm you can control the direction of the 2 motors attached to the motor controller.
		```
		>>> chan_list_output = [11,12]
		>>> GPIO.output(chan_list_output, GPIO.LOW) # Sets all to low.
		>>> 
		
		```
	* Note: this sets 1st to low, 2nd to high:
	
		```GPIO.output(chan_list_output, GPIO.LOW, GPIO.HIGH)```


1. ## Input - TO DO
	* Read the value of a GPIO pin
	* This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
	* e.g. confirm you can read the input pins from the motor controller.
		```
		>>> chan_list_input = [9,10]
		>>> GPIO.input(chan_list_input[0]) # Reading input channel 9, test if it returns "GPIO.LOW".
		>>> GPIO.LOW
		>>>
		
		```
	
1. ## Cleanup - TO DO
	Returning all channels you have used back to inputs with no pull up/down to avoid accidental damage to your RPi by shorting out the pins.
	```
	>>> GPIO.cleanup()
	>>>

	```