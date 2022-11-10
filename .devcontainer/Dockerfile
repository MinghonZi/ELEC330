FROM osrf/ros:noetic-desktop-focal AS base

SHELL ["/bin/bash", "-c"]

ARG USERNAME=elec330
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --shell /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    # Clean up
    && rm -rf /var/lib/apt/lists/*
# Set the default user
USER $USERNAME

RUN echo '[ -f /opt/ros/$ROS_DISTRO/setup.bash ] && source /opt/ros/$ROS_DISTRO/setup.bash' >> ~/.bashrc
RUN echo '[ -f /catkin_ws/devel/setup.bash ] && source /catkin_ws/devel/setup.bash' >> ~/.bashrc

RUN sudo apt-get update && sudo apt-get install --yes --no-install-recommends \
        # https://classic.gazebosim.org/tutorials?tut=ros_installing
        ros-$ROS_DISTRO-gazebo-ros-pkgs ros-$ROS_DISTRO-gazebo-ros-control \
        python-is-python3 \
        liburdfdom-tools \
    && sudo rm -rf /var/lib/apt/lists/*

# Workaround: https://answers.gazebosim.org/question/8577/gazebo-22-cant-open-usrsharegazebosetupsh/?answer=21515#post-id-21515
# Fix not merged: https://github.com/ros-simulation/gazebo_ros_pkgs/pull/1100/commits/7d0ed4ceeea0c77a606ca59c539aa8d5d7e56dc8
RUN sudo sed -i '/setup_path=/ s|$(pkg-config --variable=prefix gazebo)|/usr|' /opt/ros/noetic/lib/gazebo_ros/{gazebo,gzserver,gzclient}

RUN mkdir -p ~/catkin_ws/src
