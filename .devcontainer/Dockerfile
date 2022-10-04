FROM osrf/ros:noetic-desktop-focal AS base

WORKDIR /catkin_ws/src

RUN echo '[ -f /opt/ros/$ROS_DISTRO/setup.bash ] && source /opt/ros/$ROS_DISTRO/setup.bash' >> ~/.bashrc
RUN echo '[ -f /catkin_ws/devel/setup.bash ] && source /catkin_ws/devel/setup.bash' >> ~/.bashrc

RUN apt-get update && apt-get install --yes --no-install-recommends \
        # https://classic.gazebosim.org/tutorials?tut=ros_installing
        ros-$ROS_DISTRO-gazebo-ros-pkgs ros-$ROS_DISTRO-gazebo-ros-control \
    && rm -rf /var/lib/apt/lists/*


FROM base AS devel

RUN apt-get update && apt-get install --yes --no-install-recommends \
        curl \
        wget \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /root/.profile && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /root/.profile

RUN /home/linuxbrew/.linuxbrew/bin/brew install \
        jesseduffield/lazygit/lazygit \
        gdb

# cyrus-and/gdb-dashboard
RUN wget -P ~ https://git.io/.gdbinit && /home/linuxbrew/.linuxbrew/bin/pip3 install pygments

# Compile and install GDB
# RUN apt-get update && apt-get install --yes --no-install-recommends \
#         libncurses-dev \
#         python3-pip \
#         libgmp-dev \
#     && wget 'http://ftp.gnu.org/gnu/gdb/gdb-12.1.tar.gz' --directory-prefix=/tmp \
#     && tar -xvzf /tmp/gdb-12.1.tar.gz --directory /tmp \
#     && cd /tmp/gdb-12.1 \
#     && ./configure --enable-tui --with-python=$(which python3) \
#     && make && make install \
#     # cyrus-and/gdb-dashboard
#     && wget -P ~ https://git.io/.gdbinit && pip install pygments \
#     && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*
