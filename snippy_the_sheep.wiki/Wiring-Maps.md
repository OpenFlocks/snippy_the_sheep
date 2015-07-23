# Raspberry Pi GPIO / Motor Connections
## Setup
1. Connect 2 x 6v DC motors to [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php?title=File:DRI0002_pinout.png)
1. Connect RPi -> Breadboard -> Dual Motor Controller (see Mappings table below).
1. Connect 7.5V: +ve to VS, -ve to GND.
## Mappings
Use this table when wiring the [RPi -> Breadboard](https://howto8165.files.wordpress.com/2014/08/rpi-pinout.png) -> [Dual Motor Controller](http://www.dfrobot.com/wiki/index.php?title=File:DRI0002_pinout.png).

|Raspberry Pi GPIO Pin|Extension Board Pin|Dual Motor Controller Connection        |
|---------------------|-------------------|----------------------------------------|
|13 (GPIO27)          |P2                 |E1 (PWM 0-255 i.e. motor 1 speed)       |
|15 (GPIO22)          |P3                 |M1 (0 fwd, 1 rev i.e. motor 1 direction)|
|16 (GPIO23)          |P4                 |E2 (PWM 0-255 i.e. motor 2 speed)       |
|18 (GPIO24)          |P5                 |M2 (0 fwd, 1 rev i.e. motor 2 direction)|
|20 (GND)             |GND                |GND                                     |
