#!/usr/bin/env python  
import rospy

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg


def message_from_transform(T):
    msg = geometry_msgs.msg.Transform()
    q = tf.transformations.quaternion_from_matrix(T)
    translation = tf.transformations.translation_from_matrix(T)
    msg.translation.x = translation[0]
    msg.translation.y = translation[1]
    msg.translation.z = translation[2]
    msg.rotation.x = q[0]
    msg.rotation.y = q[1]
    msg.rotation.z = q[2]
    msg.rotation.w = q[3]
    return msg


def publish_transforms():

    # 1. base_frame to object_frame
    object_transform = geometry_msgs.msg.TransformStamped()

    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"

    T1 = tf.transformations.concatenate_matrices(
        tf.transformations.quaternion_matrix(
            tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)),
        tf.transformations.translation_matrix((0.0, 1.0, 1.0))
    )

    object_transform.transform = message_from_transform(T1)

    broadcaster.sendTransform(object_transform)

    # 2. base_frame to robot_frame
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"

    T2 = tf.transformations.concatenate_matrices(
        tf.transformations.quaternion_matrix(
            tf.transformations.quaternion_about_axis(1.57, (0, 0, 1))),
        tf.transformations.translation_matrix((0.0, -1.0, 0.0))
    )

    robot_transform.transform = message_from_transform(T2)

    broadcaster.sendTransform(robot_transform)

    # 3. robot_frame to camera_frame
    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"

    T3 = tf.transformations.concatenate_matrices(
        tf.transformations.translation_matrix((0.0, 0.1, 0.1)),
        tf.transformations.quaternion_matrix(
            tf.transformations.quaternion_about_axis(1.57, (0.0, -1.314, 0.9)))
    )

    camera_transform.transform = message_from_transform(T3)

    broadcaster.sendTransform(camera_transform)


if __name__ == '__main__':
    rospy.init_node('my_static_tf2_broadcaster')

    broadcaster = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
