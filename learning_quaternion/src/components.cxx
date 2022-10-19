#include <ros/ros.h>
#include <tf2/LinearMath/Quaternion.h>

auto main() -> int {
    tf2::Quaternion quaternion;
    quaternion.setRPY(0, 0, 0);
    // quaternion.normalize();
    ROS_INFO_STREAM(  // prints the quaternion components (0,0,0,1)
         "x: " << quaternion.getX() <<
        " y: " << quaternion.getY() <<
        " z: " << quaternion.getZ() <<
        " w: " << quaternion.getW());
};
