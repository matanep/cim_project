#Imports:
import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time
import datetime


class NaoNode(): #This class will connect to nao api and send the commands.
    def __init__(self):
        for i in range(100,200,1):#Use brute force to find nao in the local net.
            self.robotIP = '192.168.0.'+str(i)
            # self.robotIP = '192.168.0.107'
            self.port = 9559

            try:#if this doesn't work it will check the next ip.
                self.motionProxy = ALProxy("ALMotion", self.robotIP, self.port)#connect to motion API(fall if ip is not correct)
                self.audioProxy = ALProxy("ALAudioPlayer", self.robotIP, self.port)#connect to audio API(fall if ip is not correct)
                self.postureProxy = ALProxy("ALRobotPosture", self.robotIP, self.port)#connect to posture API(fall if ip is not correct)
                self.managerProxy = ALProxy("ALBehaviorManager", self.robotIP, self.port)#connect to manager API(fall if ip is not correct)
                self.tts = ALProxy("ALTextToSpeech", self.robotIP, self.port)#connect to text to speech API(fall if ip is not correct)
                break#if works - stop the loop

            except Exception,e:
                if i==200:#if try 200, something is wrong
                    print "Could not create proxy to ALMotion"
                    print "Error was: ",e
                    sys.exit(1)


        # give a feedback that the robot is connected
        self.robotConfig = self.motionProxy.getRobotConfig()
        self.motionProxy.setStiffnesses("Body", 1.0)
        self.postureProxy.goToPosture("StandInit", 0.5)
        self.motionProxy.setCollisionProtectionEnabled('Arms', True)
        self.motionProxy.post.angleInterpolationWithSpeed(['HeadPitch'], [-0.5], 0.2)

    # initialize a listener to the brain
    def start(self):
        rospy.init_node('nao_listener')                          #name of node
        rospy.Subscriber('robot_language', String, self.language)#listen to robot_language and run self.language with the data
        rospy.Subscriber("robot_command", String, self.worker)   #listen to robot_command and run self.worker with the data
        rospy.spin()#listen always

    # This is responsible to give the robot a command every time the brain publishers
    def worker(self, data):
        behavior_and_text_str=data.data
        behavior_and_text_list=behavior_and_text_str.split(";")#split the str
        behavior=behavior_and_text_list[0]                     #firs part is the behavior.
        text=behavior_and_text_list[1]                         #secont part is the text to say.
        self.do_behavior(behavior)                             #run behavior in nao
        self.say(text)                                         #say text in API

    def language(self, data):#config the language of nao
        if 'English' in data.data:
            self.tts.setLanguage('English')
        elif 'Spanish' in data.data:
            self.tts.setLanguage('Spanish')


    def do_behavior(self,behaviorName):#send API for behavior
        self.managerProxy.post.runBehavior(behaviorName)


    def say(self,text):#send API for tts
        self.tts.say(text)



nao = NaoNode()#Crate an instance of the class.
nao.start()#start running.