cmake_minimum_required(VERSION 3.0.2)
project(ass2)

find_package(catkin REQUIRED)

catkin_package()

catkin_install_python(PROGRAMS
  nodes/face_detector.py
  nodes/object_detector.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  launch
  maps
  params
  rviz
  weights
  worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
