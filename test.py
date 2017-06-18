import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time
import datetime

robotIP='192.168.0.106'
port=9559

motionProxy = ALProxy("ALMotion", robotIP, port)
audioProxy = ALProxy("ALAudioPlayer", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
managerProxy = ALProxy("ALBehaviorManager", robotIP, port)
tts = ALProxy("ALTextToSpeech", robotIP, port)

tts.say('hey adir hahahahahahaha')
managerProxy.post.runBehavior('introduction_all_0-ba154e')
tts.say('hola, como estas')

tts.setLanguage('Spanish')
tts.say('hola, como estas')
tts.setLanguage('English')