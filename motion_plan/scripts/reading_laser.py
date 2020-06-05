#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
    regions = [
        min(msg.ranges[0:143]),
        min(msg.ranges[144:287]),
        min(msg.ranges[288:431]),
        min(msg.ranges[432:575]),
        min(msg.ranges[576:719]),
    ]
    rospy.loginfo_throttle(10, regions)


def main():
    rospy.init_node("reading_laser")
    sub = rospy.Subscriber("/aster/laser/scan", LaserScan, callback_laser)
    rospy.spin()



if __name__ == "__main__":
    main()