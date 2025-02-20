# ROS2-AerialRobotics
This repository contains all the necessary code, ROS 2 packages, Docker setups, and simulation files for the Aerial Robotics course. It serves as a structured workspace for students to follow along, experiment, and develop their own aerial robotics applications.

## PX4-Autopilot

On the aerial_robotics directory install the following
repository:
1. Download PX4 Source Code

```
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
```
**DON'T isntall packages with ubuntu.sh, you need to install all packages inside container** 

## Docker installation - LINUX
1. Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Install the last version
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
3. Verify that Docker has been set up correctly by running a sample container
```bash
sudo docker run hello-world
```
## Launch containers

Launch the container
```
docker compose up -d
```
Once the container is running, you need open the terminal number needed with:
```
docker exec -it px4_ros2 bash
```

## Next Steps
Now you can navigate to the directory inside your container with

```
cd src/aerial_robotics/
```

And you can start to build PX4-Autopilot and install qgroundocntrol, Micro-XRCE-DDS-Agent, px4_msgs and inside multirortor_ws/src/ directory the px4_msgs for communication

## Launch Simulation with ROS2

Terminal 1 (PX4-Simulation)
```
make px4_sitl gz_x500
```

Terminal 2 (Micro-XRCE-DDS-Agent)
```
MicroXRCEAgent udp4 -p 8888
```
Terminal 3 (Qgroundcontrol)
```
chmod +x ./QGroundControl.AppImage
./QGroundControl.AppImage
```
Termianl 4 (ROS2)
You can use all ros2 command
```
ros2 pkg list
ros2 topic list
colcon build
source install/setup.bash
ros2 pkg create ...
...
```


## Clarifications

**Note:** This Docker setup is currently under development and may undergo changes. Please check back for updates. If you are testing the development environment, please, let me know how to improve it.

- Maintainer: Javier Herrera
- email: javier.herrera@upb.edu.co