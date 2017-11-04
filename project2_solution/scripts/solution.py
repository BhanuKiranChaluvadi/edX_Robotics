#!/usr/bin/env python  
import rospy

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg

import numpy


# The transform from the 'base' coordinate frame to the 'object' coordinate frame consists of a rotation expressed
# as (roll, pitch, yaw) of (0.79, 0.0, 0.79) followed by a translation of 1.0m along the resulting y-axis and 1.0m
# along the resulting z-axis.


# The transform from the 'base' coordinate frame to the 'robot' coordinate frame consists of a rotation around the
# z-axis by 1.5 radians followed by a translation along the resulting y-axis of -1.0m.
#
# The transform from the 'robot' coordinate frame to the 'camera' coordinate frame must be defined as follows:
#     1. The translation component of this transform is (0.0, 0.1, 0.1)
#     2. The rotation component of this transform must be set such that the camera is pointing directly at the object.
#     In other words, the x-axis of the 'camera' coordinate frame must be pointing directly at
#     the origin of the 'object' coordinate frame.

def publish_transforms():
    # 1. base_frame to object_frame
    object_transform = geometry_msgs.msg.TransformStamped()

    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"

    object_transform.transform.translation.x = 0.0
    object_transform.transform.translation.y = 1.0
    object_transform.transform.translation.z = 1.0

    q1 = tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)
    object_transform.transform.rotation.x = q1[0]
    object_transform.transform.rotation.y = q1[1]
    object_transform.transform.rotation.z = q1[2]
    object_transform.transform.rotation.w = q1[3]

    broadcaster.sendTransform(object_transform)

    # 2. base_frame to robot_frame
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"

    robot_transform.transform.translation.x = 0.0
    robot_transform.transform.translation.y = -1.0
    robot_transform.transform.translation.z = 0.0

    q2 = tf.transformations.quaternion_about_axis(1.5, (0.0, 0.0, 1))
    robot_transform.transform.rotation.x = q2[0]
    robot_transform.transform.rotation.y = q2[1]
    robot_transform.transform.rotation.z = q2[2]
    robot_transform.transform.rotation.w = q2[3]

    broadcaster.sendTransform(robot_transform)

    # 3. robot_frame to camera_frame
    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"

    camera_transform.transform.translation.x = 0.0
    camera_transform.transform.translation.y = 0.1
    camera_transform.transform.translation.z = 0.1

    q3 = tf.transformations.quaternion_about_axis(1.5, (0.0, 0.0, 1))
    camera_transform.transform.rotation.x = q3[0]
    camera_transform.transform.rotation.y = q3[1]
    camera_transform.transform.rotation.z = q3[2]
    camera_transform.transform.rotation.w = q3[3]

    broadcaster.sendTransform(camera_transform)


if __name__ == '__main__':
    rospy.init_node('my_static_tf2_broadcaster')

    broadcaster = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
