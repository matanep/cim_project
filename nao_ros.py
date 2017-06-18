import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time
import datetime


class NaoNode():
    def __init__(self):
        self.robotIP = '192.168.0.100'
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
        self.nao_movements = rospy.Publisher ('nao_movements', String)
        self.robot_running = True

        self.counter=0


    def start(self):
        #init a listener to kinect and
        rospy.init_node('nao_listener')
        rospy.Subscriber('language', String, self.language)
        rospy.Subscriber("the_flow", String, self.worker())
        rospy.Subscriber("text_to_say", String, self.say())
        rospy.spin()


    def worker(self, data):
        if 'the end' in data.data:
            self.motionProxy.rest()
            self.robot_running = False

    def language(self, data):
        if 'English' in data.data:
            self.tts.setLanguage('English')
        elif 'Spanish' in data.data:
            self.tts.setLanguage('Spanish')


    def do_behavior(self,behaviorName):
        launchAndStopBehavior(self.managerProxy, behaviorName)


    def say(self,data):
        self.tts.say(data.data)



nao = NaoNode()
nao.start()