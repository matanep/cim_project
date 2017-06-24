#Imports:
import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys
import redis



class Redis():#this class reads the redis database and sending the information to the brain.

    def __init__(self):#initialize a Publisher to the brain
        rospy.init_node('redis_publisher')#name of node
        self.lang = rospy.Publisher ('language', String)#Publish language as str
        self.flow = rospy.Publisher ('the_flow', String)#Publish the_flow as str
        self.uname = rospy.Publisher ('name', String)#Publish name as str
        self.flag=True#use flag to run a while loop

        self.initialize()

    def initialize(self):#initialize a listener to redis
        self.language='empty'  #use global variables to compare later on
        self.the_flow='empty'  #use global variables to compare later on
        self.name='empty'      #use global variables to compare later on
        self.r = redis.StrictRedis('localhost', 6379, 1, decode_responses=True, charset='utf-8')#conect to redis instance

        self.redis_listener()#run listener

    def redis_listener(self):#the listener publishes only if there was a change in redis
        while self.flag:#ever running loop
            language = self.r.get('lang:') #get from redis
            the_flow = self.r.get('state:')#get from redis
            name=self.r.get('name:')       #get from redis


            if language!=self.language:         #if new is different than the old:
                self.language=language          #update old
                print language                  #print for debug
                self.lang.publish(language)     #publish data

            if name != self.name:           #if new is different than the old:
                self.name = name            #update old
                print name                  #print for debug
                self.uname.publish(name)    #publish data

            if the_flow!=self.the_flow:     #if new is different than the old:
                self.the_flow=the_flow      #update old
                print the_flow              #print for debug
                self.flow.publish(the_flow) #publish data

app = Redis()#Crate an run an instance of the class.



