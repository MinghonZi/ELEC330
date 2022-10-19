cmake_minimum_required(VERSION 3.0.2)
project(learning_quaternion)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    tf2
    tf2_geometry_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES learning_quaternion
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

include_directories(
# include
${catkin_INCLUDE_DIRS}
)

add_executable(components src/components.cxx)
target_link_libraries(components
  ${catkin_LIBRARIES}
)
