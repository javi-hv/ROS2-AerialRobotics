# Start image from ROS2 humble-desktop with ubuntu 22.04
FROM osrf/ros:humble-desktop

# Download and install uXRCE-DDS-Agent

RUN git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
RUN /bin/bash -c 'cd Micro-XRCE-DDS-Agent; mkdir build; cd build; cmake ..; make; sudo make install; sudo ldconfig /usr/local/lib/;'

# RUN usermod -a -G dialout $USER && \
#     apt-get remove modemmanager -y && \
#     apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y && \
#     apt install libfuse2 -y && \
#     apt install libxcb-xinerama0 libxkbcommon-x11-0 libxcb-cursor-dev -y && \
#     wegt https://d176tv9ibo4jno.cloudfront.net/latest/QGroundControl.AppImage
#     # chmod +x QGroundControl.AppImage