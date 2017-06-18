import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys
import redis



class Redis():

    def __init__(self):
        rospy.init_node('redis_publisher')
        self.lang = rospy.Publisher ('language', String)
        self.flow = rospy.Publisher ('the_flow', String)
        self.name = rospy.Publisher ('name', String)
        self.flag=True

        self.initialize()

    def initialize(self):
        self.language=str
        self.the_flow=str
        self.name=str
        self.r = redis.StrictRedis('localhost', 6379, 0, decode_responses=True, charset='utf-8')

        self.redis_listener()

    def redis_listener(self):
        while self.flag:
            language = self.r.get('language' + ':kivun') #todo
            the_flow = self.r.get('language' + ':kivun') #todo
            name=self.r.get('language' + ':kivun')       #todo


            if language!=self.language:
                self.language=language
                self.lang.publish(language)

            if name != self.name:
                self.name = name
                self.name.publish(name)

            if the_flow!=self.the_flow:
                self.the_flow=the_flow
                self.flow.publish(the_flow)

app = Redis()


