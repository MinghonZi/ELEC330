
http://wiki.ros.org/roslaunch/XML/remap
http://wiki.ros.org/roslaunch/XML/node

https://answers.ros.org/question/207771/custom-rosdepyaml-in-my-package/
http://docs.ros.org/en/independent/api/rosdep/html/contributing_rules.html
https://answers.ros.org/question/221471/triggering-pip-requirementstxt-from-catkin-build/
https://www.mathworks.com/help/supportpkg/robotmanipulator/ug/install-ros-dependencies.html
```
rosdep custom rule
--------------------
yolov5-requirements:
  ubuntu:
    pip:
      packages:
        - gitpython
        - ipython
        - matplotlib
        - numpy
        - opencv-python
        - Pillow
        - psutil
        - PyYAML
        - requests
        - scipy
        - thop
        - torch
        - torchvision
        - tqdm
        - tensorboard
        - pandas
        - seaborn
```

`shopt`

http://wiki.ros.org/teleop_twist_keyboard

[PlotJuggler](https://discourse.ros.org/t/rqt-in-ros2/6428/10)

https://answers.ros.org/question/341313/what-happens-if-i-use-c-17-features-in-my-ros-nodes/

## Hardware acceleration

[WSL2 + Docker + OpenGL + NVIDIA not working (uses llvmpipe)](https://github.com/NVIDIA/nvidia-docker/issues/1554)

[OpenGL and Mesa](https://wiki.archlinux.org/title/OpenGL)

Important!!!: [NVIDIA_DRIVER_CAPABILITIES](https://github.com/NVIDIA/nvidia-container-runtime#nvidia_driver_capabilities)

```shell
apt install mesa-utils
glxinfo -B
```

> glxgears is somewhat outdated. Try better es2gears from the mesa-utils-extra package.
```shell
apt install mesa-utils-extra
es2gears
```


## Classic Gazebo

- [Components](https://classic.gazebosim.org/tutorials?tut=components&cat=get_started)
- [roslaunch](https://classic.gazebosim.org/tutorials?tut=ros_roslaunch&cat=connect_ros)
- https://classic.gazebosim.org/tutorials?tut=ros_gzplugins
- https://github.com/ros-simulation/gazebo_ros_pkgs
- https://classic.gazebosim.org/tutorials?tut=ros_control

Add eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv) to `~/.bashrc` not `~/.bash_profile` or `~/.profile`
[](https://github.com/Homebrew/brew/issues/6033)

[postCreateCommands script](https://github.com/microsoft/vscode-remote-release/issues/3527#issuecomment-674739457)

[3D model dataset for Gazebo](https://data.nvision2.eecs.yorku.ca/3DGEMS/)

The difference between the two can be summed up in the following excerpt from Morgan Quigley (one of the original developers of ROS) in his book Programming Robots with ROS:
> rviz shows you what the robot thinks is happening, while Gazebo shows you what is really happening.

[Why not using GitHub LFS](https://news.ycombinator.com/item?id=27135548)

https://github.com/bulletphysics/bullet3/tree/master/data

https://en.wikipedia.org/wiki/Mobile_manipulator

https://github.com/nicrusso7/rex-gym/blob/master/rex_gym/util/pybullet_data/assets/urdf/rex_arm.urdf
Manipulator, [Poppy Ergo Jr](https://github.com/poppy-project/poppy_ergo_jr_description)
[RoboPeak LiDAR](http://www.robopeak.com/blog/?cat=5)

Ctrl+D

https://code.visualstudio.com/docs/getstarted/userinterface#_zen-mode
Ctrl+K Z: Zen mode
Centered editor layout

[[ERROR] No p gain specified for pid.](https://answers.ros.org/question/293830/what-is-the-fix-for-no-p-gain-specified-for-pid-namespace-gazebo_ros_controlpid_gainsback_right_wheel_joint-ros-melodic/?answer=317092#post-id-317092)