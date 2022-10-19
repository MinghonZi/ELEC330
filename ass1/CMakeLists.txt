cmake_minimum_required(VERSION 3.0.2)
project(ass1)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  urdf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ass1
#  CATKIN_DEPENDS roscpp urdf
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
