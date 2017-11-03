#!/usr/bin/env python  
import random

import rospy
# from std_msgs.msg import Int16
# from project1_solution.msg import TwoInts
from project1_solution_msgs.msg import TwoInts


class Talker:
    # Must have __init__(self) function for a class, similar to a C++ class constructor
    def __init__(self):
        rate = rospy.Rate(0.5)
        pub = rospy.Publisher('two_ints', TwoInts, queue_size=10)
        # Set the message to publish as our custom message.
        msg = TwoInts()
        # Main while loop.
        while not rospy.is_shutdown():
            # Initialize message variables.
            msg.a = random.randint(1, 20)
            msg.b = random.randint(1, 20)
            pub.publish(msg)
            rate.sleep()


if __name__ == '__main__':
    # Initialize the node and name it
    rospy.init_node('two_int_talker', anonymous=False)
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass
