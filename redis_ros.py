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
        self.uname = rospy.Publisher ('name', String)
        self.flag=True

        self.initialize()

    def initialize(self):
        self.language='empty'
        self.the_flow='empty'
        self.name='empty'
        self.r = redis.StrictRedis('localhost', 6379, 1, decode_responses=True, charset='utf-8')

        self.redis_listener()

    def redis_listener(self):
        while self.flag:
            language = self.r.get('lang:')
            the_flow = self.r.get('state:')
            name=self.r.get('name:')


            if language!=self.language:
                self.language=language
                print language
                self.lang.publish(language)

            if name != self.name:
                self.name = name
                print name
                self.uname.publish(name)

            if the_flow!=self.the_flow:
                self.the_flow=the_flow
                print the_flow
                self.flow.publish(the_flow)

app = Redis()


#$ sudo /usr/local/bin/redis-server /etc/redis/redis.conf
