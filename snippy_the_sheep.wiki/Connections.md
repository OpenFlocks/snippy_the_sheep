# Connections
1. ## Raspberry Pi Setup Test
	1. ### Parts
		1. 1 x [Raspberry Pi 1 Model B](https://www.raspberrypi.org/products/model-b/).
		1. 1 x [Raspberry-Pi-GPIO Extension Board v2.1](http://www.ebay.com.au/itm/Extension-Board-V2-1-GPIO-Adapter-Module-for-Raspberry-Pi-/391178924561?pt=LH_DefaultDomain_15&hash=item5b1414b211).
		1. 1 x Small breadboard.
		1. 1 x 470K resistor.
		1. 1 x Green LED.
		1. 1 x wire (male ends).
	1. ### Breadboard
		1. Connect GPIO cable to Extension Board.
		1. Connect Extension Board to breadboard.
		1. Connect resistor, green LED, wire.
			* See table below and [image](https://github.com/OpenFlocks/snippy_the_sheep/blob/master/develop/hardware/breadboard_led_connection.jpg).
	1. ### RPi
		1. Insert SD card built with [Snippy's Brain](https://github.com/OpenFlocks/snippy_the_sheep/blob/master/snippy_the_sheep.wiki/ROS-Setup.md#installing-ros-on-rpi).
		1. Connect GPIO cable to RPi (to later connect to Extension Board).
		1. Connect to internet (ethernet cable or usb wifi adaptor).
		1. Connect power (mains adaptor or battery).
		1. Remote login (via ssh) to Snippy's Brain from your Laptop.
		1. Download the [doctest](https://github.com/OpenFlocks/snippy_the_sheep/blob/master/snippy_the_sheep.wiki/test_rpi_gpio_setup.md) and run ...
			```
			pi@raspberrypi~/scripts $ sudo python -m doctest -v test_rpi_gpio_setup.md﻿
			```
			* Observe LED turn on (3 seconds), off, then pulse.
			* Any problems will show in your shell i.e test failures will help you trouble-shoot your setup.
		1. Shutdown RPi.
			```
			pi@raspberrypi ~/scripts $ sudo shutdown -Ph now
			```

		|Raspberry Pi GPIO Pin|Extension Board Pin|Breadboard Cell|Component    |
		|---------------------|-------------------|---------------|-------------|
		|7 (GPIO4)            |P7                 |G11 + I11      |Resistor 470K|
		|-                    |-                  |J11 + -ve rail |Green LED    |
		|-                    |GND                |I12 + -ve rail |Wire         |
	
1. ## Raspberry Pi GPIO / Dual Motor Controller Setup 
	* This setup assumes you have successfully completed the Raspberry Pi Setup Test above.
	1. ### Parts
		1. 2 x 6v DC motors.
		1. 9 x wires (male ends: 2 red, 3 black, 2 green, 2 yellow).
		1. 1 x [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php/MD1.3_2A_Dual_Motor_Controller_SKU_DRI0002).
		1. 1 x max 12v / max 2A power supply.
	1. ### RPi
		1. Connect RPi -> Breadboard -> Dual Motor Controller (see Mappings table below).
	1. ### [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php/MD1.3_2A_Dual_Motor_Controller_SKU_DRI0002)
		1. Connect 2 x 6v DC motors to M1 and M2.
		1. Leave Jumper connected i.e. VS (motor power supply) == VD (board power supply)
			* **IMPORTANT**: Board power maximum of 12v. If motors need > 12v, disconnect Jumper (i.e. makes VS != VD power) and provide separate power supplies for board (via VD connection) + motor (via VS connection).
		1. Connect power (mains adaptor or battery) leads to VS + GND.
	1. ### Test From RPi
		1. Connect power to RPi.
		1. ```scp``` the code directory ```~/catkin_ws/src/snippy_the_sheep``` from Laptop to ROS catkin workspace location on RPi.
		1. Build ROS environment on RPi by running ```catkin_make```
			1. Takes about 30 minutes!
		1. Replace ```Defaults env_reset``` with ```Defaults env_keep += "PYTHONPATH"``` in ```/etc/sudoers``` via ```sudo visudo```.
		1. Run ```roscore``` in terminal 1  (non-root user), ```drive.py``` in terminal 2 (root user) and then ```brain.py``` in terminal 3 (root user).

		1. Run test as root.
			```
			sudo su
			source /opt/ros/indigo/devel/setup.bash
			python drive.py # aka in terminal 2
			...
			python brain.py # aka in terminal 3
			```
			You should see motors spin forward, stop, then spin backward.
		1. TO DO: write [doctest](https://waffle.io/OpenFlocks/snippy_the_sheep/cards/55b16501ab5c863200b41cd1).
		1. Shutdown RPi.
			```
			pi@raspberrypi ~/scripts $ sudo shutdown -Ph now
			```
	1. ### Mappings
		Use this table when wiring the [RPi -> Breadboard](https://howto8165.files.wordpress.com/2014/08/rpi-pinout.png) -> [Dual Motor Controller](http://www.dfrobot.com/wiki/images/1/10/DRI0002_pinout.png).
		
		|Raspberry Pi GPIO Pin|Extension Board Pin|Breadboard Cell|Dual Motor Controller Connection        |Wire Colour|
		|---------------------|-------------------|---------------|----------------------------------------|-----------|
		|13 (GPIO27)          |P2                 |J6             |E1 (PWM 0-255 i.e. motor 1 speed)       |Green      |
		|15 (GPIO22)          |P3                 |J7             |M1 (0 fwd, 1 rev i.e. motor 1 direction)|Yellow     |
		|16 (GPIO23)          |P4                 |J8             |E2 (PWM 0-255 i.e. motor 2 speed)       |Green      |
		|18 (GPIO24)          |P5                 |J9             |M2 (0 fwd, 1 rev i.e. motor 2 direction)|Yellow     |
		|-                    |-                  |-ve rail       |GND                                     |Black      |
		|20 (GND)             |GND                |J12 + -ve rail |-                                       |White      |