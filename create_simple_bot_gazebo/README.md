### create_simple_bot_gazebo

```diff
# Importing the model in Gazebo
+ The model in the `simple_bot` folder is created using the Gazebo tutorial to make a mobile robot:
+ https://gazebosim.org/tutorials?tut=build_robot&cat=build_robot
+ Before the model can be imported in Gazebo, we need to have Gazebo running.
+ The model can be imported through the Insert Model interface in Gazebo:
+ https://gazebosim.org/tutorials?tut=build_world&cat=build_world#AddingModelfromtheModelDatabase

- Note: An easy way to ensure that everything will work as expected is to use Docker.
- If using Ubuntu and an NVIDIA graphics card, use this link to install Docker:
- https://docs.docker.com/engine/install/ubuntu/
- and this link to install NVIDIA Container Toolkit:
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit
- Then, we can create a docker image using the `Dockerfile` present in the `docker_files` folder.
- Refer to the `README.md` inside the `docker_files` folder for more info.
- After the image is created, we can run containers using this image and run Gazebo from this container.
```
