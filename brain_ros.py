import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys


class Brain_Node():
    def __init__(self):
        self.robot_command = rospy.Publisher ('robot_command', String)
        self.robot_language = rospy.Publisher ('robot_language', String)

        self.ulanguage=str
        self.name=str
        print 'here'
        self.start()




    def start(self):
        #init a listener to kinect and
        rospy.init_node('brain')
        rospy.Subscriber('language', String, self.language)
        rospy.Subscriber("name", String, self.name)
        rospy.Subscriber("the_flow", String, self.robot_behavior)
        print 'here'
        rospy.spin()



    def robot_behavior(self, data):
        text=str
        behavior=str
        if 'hello' in data.data:
            print '1111'
            behavior='Stand/Gestures/Hey_6'
            if self.language=='English':
                text='hello, my name is Rami amd I will help you'
            else:
                text='Hola, mi nombre es Rami y yo te ayudare'
            pub=self.make_str(behavior,text)
            self.robot_command.publish(pub)


    def language(self, data):
        print 'hrhe'
        if 'english' in data.data:
            self.ulanguage='English'
            self.robot_language.publish('English')
        elif 'spanish' in data.data:
            self.ulanguage='Spanish'
            self.robot_language.publish('Spanish')

    def name(self,data):
        self.name=data.data

    def make_str(self,behavior=str,text=str):
        return behavior +";" +text

goosmart=Brain_Node()