import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time
import datetime


class NaoNode():
    def __init__(self):
        self.robotIP = '192.168.0.104'
        self.port = 9559

        try:
            self.motionProxy = ALProxy("ALMotion", self.robotIP, self.port)
            self.audioProxy = ALProxy("ALAudioPlayer", self.robotIP, self.port)
            self.postureProxy = ALProxy("ALRobotPosture", self.robotIP, self.port)
            self.managerProxy = ALProxy("ALBehaviorManager", self.robotIP, self.port)
            self.tts = ALProxy("ALTextToSpeech", self.robotIP, self.port)

        except Exception,e:
            print "Could not create proxy to ALMotion"
            print "Error was: ",e
            sys.exit(1)

        # Get the Robot Configuration
        self.robotConfig = self.motionProxy.getRobotConfig()
        self.motionProxy.setStiffnesses("Body", 1.0)
        self.postureProxy.goToPosture("StandInit", 0.5)
        self.motionProxy.setCollisionProtectionEnabled('Arms', True)
        self.motionProxy.post.angleInterpolationWithSpeed(['HeadPitch'], [-0.5], 0.2)


        self.communicating = False
        self.robot_running = True

        self.counter=0


    def start(self):
        #init a listener to kinect and
        rospy.init_node('nao_listener')
        rospy.Subscriber('robot_language', String, self.language)
        rospy.Subscriber("robot_command", String, self.worker)
        rospy.spin()


    def worker(self, data):
        behavior_and_text_str=data.data
        behavior_and_text_list=behavior_and_text_str.split(";")
        behavior=behavior_and_text_list[0]
        text=behavior_and_text_list[1]
        self.do_behavior(behavior)
        self.say(text)

    def language(self, data):
        if 'English' in data.data:
            self.tts.setLanguage('English')
        elif 'Spanish' in data.data:
            self.tts.setLanguage('Spanish')


    def do_behavior(self,behaviorName):
        self.managerProxy.post.runBehavior(behaviorName)


    def say(self,text):
        self.tts.say(text)



nao = NaoNode()
nao.start()