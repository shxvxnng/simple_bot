FROM osrf/ros:foxy-desktop

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN curl -sSL http://get.gazebosim.org | sh

RUN apt install -y ros-foxy-navigation2

RUN apt install -y ros-foxy-nav2-bringup

RUN apt install -y ros-foxy-turtlebot3*
