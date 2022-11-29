<h1>
  ROS Dobot Driver with Python
</h1>

## Project Description


## Preparation
- Linux / Ubuntu 20.04 (recommend standalone Ubuntu or WSL for Win11)
- Install [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)

## Installation
- Place dobot_driver into the src directory of the already created catkin workspace. 
- In the Ubuntu Terminal of /your_ws/ with the /devel file, type: 
```
$ catkin_make
```

In dobot_driver/scripts, start the driver node by running
```
$ python3 dobot_server.py
```
