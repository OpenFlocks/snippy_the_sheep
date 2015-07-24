# Connections
1. ## Raspberry Pi / LED 
	1. ### Setup
		1. #### RPi
			1. Insert SD card (Snippy's brain).
			1. Connect GPIO cable to RPi (to later connect to Extension Board).
			1. Connect to internet (ethernet cable or usb wifi adaptor).
		1. ### Breadboard
			1. Connect GPIO cable to Extension Board
			1. Connect Extension Board to breadboard
			1. Connect resistor, green LED, wire.
				* See table below and [image](https://github.com/OpenFlocks/snippy_the_sheep/blob/master/develop/hardware/breadboard_led_connection.jpg).
			1. Connect power (mains adaptor or battery).
	
			|Raspberry Pi GPIO Pin|Extension Board Pin|Breadboard Cell|Component    |
			|---------------------|-------------------|---------------|-------------|
			|7 (GPIO4)            |P7                 |g11,i11        |Resistor 470K|
			|                     |                   |j11,-ve rail   |Green LED    |
			|                     |GND                |i12,-ve rail   |Wire         |
	
1. ## Raspberry Pi GPIO / Dual Motor Controller 
	1. ### Setup
		1. Connect 2 x 6v DC motors to [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php?title=File:DRI0002_pinout.png)
		1. Connect RPi -> Breadboard -> Dual Motor Controller (see Mappings table below).
		1. Connect 7.5V: +ve to VS, -ve to GND.
	1. ### Mappings
		Use this table when wiring the [RPi -> Breadboard](https://howto8165.files.wordpress.com/2014/08/rpi-pinout.png) -> [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php?title=File:DRI0002_pinout.png).
		
		|Raspberry Pi GPIO Pin|Extension Board Pin|Dual Motor Controller Connection        |
		|---------------------|-------------------|----------------------------------------|
		|13 (GPIO27)          |P2                 |E1 (PWM 0-255 i.e. motor 1 speed)       |
		|15 (GPIO22)          |P3                 |M1 (0 fwd, 1 rev i.e. motor 1 direction)|
		|16 (GPIO23)          |P4                 |E2 (PWM 0-255 i.e. motor 2 speed)       |
		|18 (GPIO24)          |P5                 |M2 (0 fwd, 1 rev i.e. motor 2 direction)|
		|20 (GND)             |GND                |GND                                     |
		