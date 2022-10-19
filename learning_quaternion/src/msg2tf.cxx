#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

auto main() -> int {
    // tf2::Quaternion quat_tf {0, 0, 0, 1};
    tf2::Quaternion quat_tf;
    geometry_msgs::Quaternion quat_msg ...;  // TODO: How to init?

    tf2::convert(quat_msg , quat_tf);
    // or
    tf2::fromMsg(quat_msg, quat_tf);
    // or for the other conversion direction
    quat_msg = tf2::toMsg(quat_tf);
};
