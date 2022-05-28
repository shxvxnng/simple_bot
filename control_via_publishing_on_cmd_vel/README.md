### control_via_publishing_on_cmd_vel

```diff
# Modifications to the model of the simple bot
+ The sdf model we used earlier:
+ https://github.com/tuffrobotics/simple_bot/blob/main/create_simple_bot_gazebo/gazebo/models/simple_bot/model.sdf
+ is modified to include the mass and inertia tensor values for the links of the robot
+ and other changes such as addition of the differential drive plugin is made.
+ This modified version of the model is present in the `simple_bot` folder.

! The changes made are inspired by this file:
! https://github.com/ros-simulation/gazebo_ros_pkgs/blob/ros2/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world

# Importing the model in Gazebo
+ We need to import this model in Gazebo but before that, we need to have Gazebo running.
+ The model can be imported through the Insert Model interface in Gazebo:
+ https://gazebosim.org/tutorials?tut=build_world&cat=build_world#AddingModelfromtheModelDatabase
+ To check if the inertia tensor is more or less correctly defined,
+ we can select "View->Inertia" from the Gazebo menu. For more details, check this link:
+ https://classic.gazebosim.org/tutorials?tut=inertia#CheckinginGazebo
+ We should see something like this:
```
<img src="https://user-images.githubusercontent.com/99809034/167256929-4e1f3265-ca89-433f-a2c6-e03e17817ca3.png" width=50% height=50%>

```diff
# Publishing a velocity
+ After that, we can deselect the same and can publish a velocity to our simple robot using the command:
ros2 topic pub /cmd_vel geometry_msgs/Twist '{linear: {x: -1.0}}' -1

+ The result will look something like this:
```
<img src="https://user-images.githubusercontent.com/99809034/167256936-9e7b27ec-dc13-4ad0-b293-da3bff6326ea.gif" width=50% height=50%>

```diff
- Note: An easy way to ensure that everything will work as expected is to use Docker.
- If using Ubuntu and an NVIDIA graphics card, use this link to install Docker:
- https://docs.docker.com/engine/install/ubuntu/
- and this link to install NVIDIA Container Toolkit:
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit
- Then, we can create a docker image using the `Dockerfile` present in the `docker_files` folder.
- Refer to the `README.md` inside the `docker_files` folder for more info.
- After the image is created, we can run containers using this image and run Gazebo and ROS nodes from these containers.
```
