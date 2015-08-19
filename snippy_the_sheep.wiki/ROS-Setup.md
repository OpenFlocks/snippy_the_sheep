---


# Installing ROS + Snippy The Sheep on RPi

## ROS
1. This [tutorial](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Indigo%20on%20Raspberry%20Pi) was tested on my RPi B Board Rev 2.

## Snippy The Sheep Code
1. Make directory in your workspace ```$mkdir ~/catkin_ws/src/snippy_the_sheep```
1. Download or fork [Snippy The Sheep code](https://github.com/OpenFlocks/snippy_the_sheep) into that directory.

---

## [WARNING: Show-stopper Device Tree Issue](https://waffle.io/OpenFlocks/snippy_the_sheep/cards/559862d0a7b4291400474126)

## Laptop + Beaglebone Black
* These are the core commands to setup ROS on Ubuntu 14.04. See [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials) for full details.

```
cd ~/
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-get update
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install ros-indigo-desktop-full
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall
sudo rosdep init
rosdep update
sudo apt-get install chrony
sudo apt-get install ros-indigo-rqt-reconfigure
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
catkin_init_workspace
cd ../
catkin_make
source ~/catkin_ws/devel/setup.bash 
rospack profile
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

## Beaglebone Black

### Loading Device Tree Overlay

* For Ubuntu 14.04 you need to install linux-image-3.8.13-bone68 to use bone_capemgr. Use following commands to install linux-image-3.8.13-bone68
```
sudo apt-get update
sudo apt-get install linux-image-3.8.13-bone68
sudo reboot
```

* Add following lines at the end of the .profile file.
```
export SLOTS=/sys/devices/bone_capemgr.9/slots
export PINS=/sys/kernel/debug/pinctrl/44e10800.pinmux/pins
```

* Check environment variables $SLOT and $PIN
```
source ~/.profile
cat $SLOTS
cat $PINS
```

## References
* [Beagleboard Getting Started](http://beagleboard.org/getting-started)
* [Beaglebone Black](http://elinux.org/Beagleboard:BeagleBoneBlack)

---
