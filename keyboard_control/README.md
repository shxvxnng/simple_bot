### keyboard_control

```diff
# Importing the model in Gazebo
+ We need to run Gazebo and load the simple robot model present in this folder:
+ https://github.com/tuffrobotics/simple_bot/tree/main/keyboard_control/gazebo/models/simple_bot
+ using the Insert Model interface in Gazebo:
+ https://gazebosim.org/tutorials?tut=build_world&cat=build_world#AddingModelfromtheModelDatabase

# Launching the velocity publisher
+ We need to navigate to the `ros` folder and run the following commands:
colcon build
. install/setup.bash 
ros2 run keyboard_control velocity_publisher

- Note: An easy way to ensure that everything will work as expected is to use Docker.
- If using Ubuntu and an NVIDIA graphics card, use this link to install Docker:
- https://docs.docker.com/engine/install/ubuntu/
- and this link to install NVIDIA Container Toolkit:
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit
- Then, we can create a docker image using the `Dockerfile` present in the `docker_files` folder.
- Refer to the `README.md` inside the `docker_files` folder for more info.
- After the image is created, we can run containers using this image and run Gazebo and ROS nodes from these containers.
```
