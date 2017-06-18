import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys


class Brain_Node():
    def __init__(self):
        self.robot_command = rospy.Publisher ('robot_command', String)
        self.robot_language = rospy.Publisher ('robot_language', String)

        self.language=str
        self.name=str

        self.start()



    def start(self):
        #init a listener to kinect and
        rospy.init_node('brain')
        rospy.Subscriber('language', String, self.language)
        rospy.Subscriber("name", String, self.name)
        rospy.Subscriber("the_flow", String, self.robot_behavior)
        rospy.spin()



    def (self, data):
        if 'the end' in data.data:
            self.motionProxy.rest()
            self.robot_running = False

    def language(self, data):
        if 'English' in data.data:
            self.language='English'
            self.robot_language.publish('English')
        elif 'Spanish' in data.data:
            self.language='Spanish'
            self.robot_language.publish('Spanish')

    def name(self):
