#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

pub = rospy.Publisher('sum', Int16, queue_size=10)


def callback(data):
    summation = data.a + data.b
    pub.publish(summation)


def listener():
    rospy.init_node('sum_two_ints', anonymous=True)
    rospy.Subscriber("two_ints", TwoInts, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
