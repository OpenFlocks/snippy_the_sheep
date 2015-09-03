# Snippy Docker Container Setup
1. ## Laptop Only Setup
	* Docker version "openflocks/snippy:latest"
		* Will soon create new tag "openflocks/snippy:laptop_latest" once Raspberry Pi 2 Setup is done (see below).
	* Deploy this to your Laptop to play with the brain.py controller.
		* ROS Nodes that depend on robot hardware (like drive.py) are commented-out of brain.py.
	1. [Install Docker for your OS](http://docs.docker.com/linux/started/)
		```
		andrew@openflocks-laptop:~/Downloads$ sudo su
		root@openflocks-laptop:/home/andrew/Downloads$ wget -qO- https://get.docker.com/ | sh		

		...

		Client:
		 Version:      1.8.1
		 API version:  1.20
		 Go version:   go1.4.2
		 Git commit:   d12ea79
		 Built:        Thu Aug 13 02:35:49 UTC 2015
		 OS/Arch:      linux/amd64
		
		Server:
		 Version:      1.8.1
		 API version:  1.20
		 Go version:   go1.4.2
		 Git commit:   d12ea79
		 Built:        Thu Aug 13 02:35:49 UTC 2015
		 OS/Arch:      linux/amd64
		
		If you would like to use Docker as a non-root user, you should now consider
		adding your user to the "docker" group with something like:
		
		  sudo usermod -aG docker your-user
		
		Remember that you will have to log out and back in for this to take effect!

		$ exit
		$ sudo usermod -aG docker andrew
		$ sudo shutdown -Ph now
		
		```
		* Confirm installation is working correctly.
			```
			andrew@openflocks-laptop:~$ docker run hello-world
			Unable to find image 'hello-world:latest' locally
			latest: Pulling from library/hello-world
			
			535020c3e8ad: Pull complete 
			af340544ed62: Already exists 
			library/hello-world:latest: The image you are pulling has been verified. Important: image verification is a tech preview feature and should not be relied on to provide security.
			
			Digest: sha256:d5fbd996e6562438f7ea5389d7da867fe58e04d581810e230df4cc073271ea52
			Status: Downloaded newer image for hello-world:latest
			
			Hello from Docker.
			This message shows that your installation appears to be working correctly.
			
			To generate this message, Docker took the following steps:
			 1. The Docker client contacted the Docker daemon.
			 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
			 3. The Docker daemon created a new container from that image which runs the
			    executable that produces the output you are currently reading.
			 4. The Docker daemon streamed that output to the Docker client, which sent it
			    to your terminal.
			
			To try something more ambitious, you can run an Ubuntu container with:
			 $ docker run -it ubuntu bash
			
			Share images, automate workflows, and more with a free Docker Hub account:
			 https://hub.docker.com
			
			For more examples and ideas, visit:
			 https://docs.docker.com/userguide/
			
			```
	1. Download latest [Snippy Container from Docker](https://hub.docker.com/r/openflocks/snippy/tags/) and run it.
		```
		docker pull openflocks/snippy
		```
	1. Terminal 1: Run the Snippy Docker image:
		```
		$ docker run -it --rm --name my_running_snippy snippy_the_sheep
	 	```
	1. Launch Snippy's brain:
		```
		root@cb579b39d8b1:/catkin_ws/src/snippy/scripts# roslaunch snippy snippy.launch
		```		
	1. Terminal 2: Start a new terminal and bash into it.
		```
		andrew@openflocks-laptop:~/catkin_ws/src/snippy/src$ docker exec -it cb579b39d8b1 bash
		root@cb579b39d8b1:/# source /catkin_ws/devel/setup.bash 
		```
	1. Terminal 3: Start another new terminal bash into it then watch for new messages in the topic.
		```
		andrew@openflocks-laptop:~/node-workshop/hello-world-website$ docker exec -it cb579b39d8b1 bash
		root@cb579b39d8b1:/# source /catkin_ws/devel/setup.bash 
		root@cb579b39d8b1:/# rostopic echo thought_topic
		```
	1. Terminal 2: Add a thought into Snippy's head.
		```
		andrew@openflocks-laptop:~/catkin_ws/src/snippy/src$ docker exec -it cb579b39d8b1 bash
		root@cb579b39d8b1:/# rostopic pub -1 thought_topic std_msgs/String "I'm inside my own Docker container!"
		publishing and latching message for 3.0 seconds
		root@cb579b39d8b1:/# 
		```
	1. Terminal 3: See the message arrive in the topic.
		```
		data: I'm inside my own Docker container!
		---
		```
	1. To restart this container:
		```
		andrew@openflocks-laptop:~/catkin_ws/src/snippy/src$ docker restart cb579b39d8b1
		```

1. ## Raspberry Pi 2 Setup
	* Docker version "openflocks/snippy:rpi2_latest"
	* Deploy this to your robot.
	1. TO DO