#! /usr/bin/env python

import rospy

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2


x = 0.0
y = 0.0
theta = 0.0


def newOdom (msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    x = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])



rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

speed = Twist()

r = rospy.Rate(4)

goal = Point()
goal.x = 5
goal.y = 5

counter = 0

while not rospy.is_shutdown():
    inc_x = goal.x - x
    inc_y = goal.y - y
    angle_to_goal = atan2(inc_y, inc_x)

    if counter < 24:
        speed.linear.x = 0.0
        speed.angular.z = -0.3
    elif counter < 30:
        speed.linear.x = 0.0
        speed.angular.z = 0.0
    elif counter < 31:
        speed.linear.x = 0.1
        speed.angular.z = 0.0
    elif counter < 32:
        speed.linear.x = 0.2
        speed.angular.z = 0.0
    elif counter < 50:
        speed.linear.x = 0.3
        speed.angular.z = 0.0
    elif counter < 60:
        speed.linear.x = 0.0
        speed.angular.z = 0.0
    elif counter < 78:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    elif counter < 90:
        speed.linear.x = 0.0
        speed.angular.z = 0.0
    elif counter < 115:
        speed.linear.x = 0.3
        speed.angular.z = -0.04
    elif counter < 116:
        speed.linear.x = 0.2
        speed.angular.z = 0.0
    elif counter < 119:
        speed.linear.x = 0.1
        speed.angular.z = 0.0
    elif counter < 125:
        speed.linear.x = 0.0
        speed.angular.z = 0.0
    elif counter < 139:
        speed.linear.x = 0.0
        speed.angular.z = -0.3
    elif counter < 155:
        speed.linear.x = 0.0
        speed.angular.z = -0.0
    elif counter < 156:
        speed.linear.x = 0.1
        speed.angular.z = -0.0
    elif counter < 157:
        speed.linear.x = 0.2
        speed.angular.z = -0.0
    elif counter < 159:
        speed.linear.x = 0.3
        speed.angular.z = -0.0
    elif counter < 167:
        speed.linear.x = 0.5
        speed.angular.z = 0.0
    else:
        speed.linear.x = 0.0
        speed.angular.z = 0.0

    pub.publish(speed)
    counter = counter + 1
    print(counter)
    r.sleep()