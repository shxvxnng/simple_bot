#!/bin/bash

XSOCK=/tmp/.X11-unix

docker run -it \
 --runtime=nvidia \
 --user=$(id -u $USER):$(id -g $USER) \
 -e DISPLAY=$DISPLAY \
 --workdir="/home/$USER" \
 --volume="/home/$USER:/home/$USER" \
 --volume="/etc/group:/etc/group:ro" \
 --volume="/etc/passwd:/etc/passwd:ro" \
 --volume="/etc/shadow:/etc/shadow:ro" \
 --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
 -v /dev/shm:/dev/shm \
 -v $XSOCK:$XSOCK \
 -v $HOME/.Xauthority:/root/.Xauthority \
 --net=host \
 --privileged \
 osrf/ros2:foxy-desktop-nvidia-gazebo-nav2
