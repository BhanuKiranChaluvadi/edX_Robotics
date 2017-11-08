#!/usr/bin/env python  
import rospy


from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

pub = rospy.Publisher('sum', Int16, queue_size=10)


def callback(data):
    summation = data.a + data.b
    pub.publish(summation)


def summer():
    # Create a subscriber with appropriate topic, custom message and name of callback function.
    rospy.Subscriber("two_ints", TwoInts, callback)
    # Wait for messages on topic, go to callback function when new messages arrive.
    rospy.spin()


if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('add_two_ints')
    # Go to the main loop.
    summer()
