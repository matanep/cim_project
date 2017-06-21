import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time
import datetime

robotIP='192.168.0.104'
port=9559

motionProxy = ALProxy("ALMotion", robotIP, port)
audioProxy = ALProxy("ALAudioPlayer", robotIP, port)
postureProxy = ALProxy("ALRobotPosture", robotIP, port)
managerProxy = ALProxy("ALBehaviorManager", robotIP, port)
tts = ALProxy("ALTextToSpeech", robotIP, port)
tts.setLanguage('English')

tts.say('hey adir hahahahahahaha')
managerProxy.post.runBehavior('Stand/Waiting/ShowSky_2')
tts.say('hola, como estas')

tts.setLanguage('Spanish')
tts.say('hola, como estas')
tts.setLanguage('English')


import redis
r = redis.StrictRedis('localhost', 6379, 1, decode_responses=True, charset='utf-8')
print r.get('lang:')



robotConfig = motionProxy.getRobotConfig()
motionProxy.setStiffnesses("Body", 1.0)
postureProxy.goToPosture("StandInit", 0.5)
motionProxy.post.angleInterpolationWithSpeed(['HeadPitch'], [-0.5], 0.2)