#Imports:
import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys

#this class is the logic behind it all, it reserve raw  input form the redis_ros and publish for the nao_ros
class Brain_Node():
    def __init__(self):                                                 #initialize a Publisher to the nao
        self.robot_command = rospy.Publisher ('robot_command', String)  #Publish robot_command as str
        self.robot_language = rospy.Publisher ('robot_language', String)#Publish robot_language as str
        self.choice=False                                                   #flag that will be used to know if a user was already in the choice screen
        self.ulanguage='English'                                        #by default the language is English, unless we get it different in the redis
        self.uname=str                                                  #will save the user name
        self.start()                                                    #run start-->


    def start(self):
        #init a listener to redis
        rospy.init_node('brain')                                    #name of node
        rospy.Subscriber('language', String, self.language)         #listen to language and run self.language with the data
        rospy.Subscriber("name", String, self.name)                 #listen to name and run self.name with the data
        rospy.Subscriber("the_flow", String, self.robot_behavior)   #listen to the_flow and run self.robot_behavior with the data
        rospy.spin()                                                #listen always



    def robot_behavior(self, data):#this will get the state from the redis_ros and will output a behavior and text
        text=str                   #will use this to save text
        behavior=str               #will use this to save behavior
        print data.data            #print for debug
        print self.ulanguage       #print for debug


        if 'empty' in data.data:  #if this is the beginning (or a new) we get all back to default
            self.choice=False     #back to default

        if 'hello' in data.data:            #if the redis pablised hello
            behavior='aom/hello'            #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='Hello, welcome to the HMO. My name is Rami, and I am here to help you....    Please select a language.'
            else:                           #if user language is not English test is in spanish
                text='Hola, bienvenido a la HMO. Mi nombre es Rami, y yo estoy aqui para ayudarle. Por favor, seleccione un idioma.'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'id_num' in data.data:           #if the redis pablised id_num
            behavior='aom/id_num'
            if self.ulanguage=='English':   #if user language is English test is in English
                text='Please Insert your ID number.'
            else:                           #if user language is not English test is in spanish
                text='Introduzca su numero de identificacion, Por favor.'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'invalid' in data.data:          #if the redis pablised invalid or ~invalid~
            behavior='aom/invalid'          #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='Oh, wrong input. Please insert again'
            else:                           #if user language is not English test is in spanish
                text='Oh, de entrada incorrecta. Por favor, inserte de nuevo'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'choice' in data.data and self.choice==True:#if the redis pablised choice and it is the first time
            behavior='aom/decision'                    #choose the right behavior
            if self.ulanguage=='English':              #if user language is English test is in English
                text='Can I help you with anything else?'
            else:                                      #if user language is not English test is in spanish
                text='Puedo ayudarle con cualquier otra cosa?'
            pub=self.make_str(behavior,text)           #make publish str
            self.robot_command.publish(pub)            #publish the str in "robot_command"

        if 'choice' in data.data and self.choice==False:#if the redis pablised choice and it is not the first time
            behavior='aom/choice'                       #choose the right behavior
            if self.ulanguage=='English':               #if user language is English test is in English
                text='Hello '+ self.uname +',' + ' Please choose the requested service.'#use the name in the text
            else:                                       #if user language is not English test is in spanish
                text='Hola '+ self.uname +',' + ' por favor seleccione el servicio solicitado.'#use the name in the text
            self.choice=True                            #change choice to True(it was visited)
            pub=self.make_str(behavior,text)            #make publish str
            self.robot_command.publish(pub)             #publish the str in "robot_command"

        if 'blood test' in data.data:       #if the redis pablised blood
            behavior='aom/up_left'          #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='The blood test room is on the 2nd floor, on the left'
            else:                           #if user language is not English test is in spanish
                text='La sala de examen de sangre esta en el segundo piso, a la izquierda'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'vaccination' in data.data:      #if the redis pablised vaccination
            behavior='aom/up_right'         #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='The vaccination room is on the 2nd floor, on the right, next to the elevator'
            else:                           #if user language is not English test is in spanish
                text='La sala de la vacunacion esta en el segundo piso, a la derecha, al lado del ascensor.'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'toilet' in data.data:           #if the redis pablised toilet
            behavior='aom/right'            #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='The toilet is on the 1st floor, on your right, next to the vending machine.'
            else:                           #if user language is not English test is in spanish
                text='El inodoro esta en el 1er piso, a la derecha, junto a la'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'reception' in data.data:        #if the redis pablised reception
            behavior='aom/left'             #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='The reception is on the 1st floor, to the left'
            else:                           #if user language is not English test is in spanish
                text='La recepcion esta en la primera planta, a la izquierda'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'finish' in data.data:           #if the redis pablised finish
            behavior='aom/finish'           #choose the right behavior
            if self.ulanguage=='English':   #if user language is English test is in English
                text='Thank you, and have a pleasant day!'
            else:                           #if user language is not English test is in spanish
                text='Gracias, y tienen un dia agradable!'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

    def language(self, data):
        if 'english' in data.data:                  #if the redis pablised english
            self.ulanguage='English'                #user language is english
            self.robot_language.publish('English')  #publish English

        elif 'spanish' in data.data:                #if the redis pablised spanish
            self.ulanguage='Spanish'                #user language is english
            self.robot_language.publish('Spanish')  #publish Spanish

        elif 'empty' in data.data:                  #if the redis pablised empty
            self.ulanguage='English'                #user language is english by default
            self.robot_language.publish('English')  #publish English

    def name(self,data):
        if 'empty' in data.data:            #if the redis pablised empty, reset name
            self.uname=str
        else:
            self.uname=data.data            #save name for use, if it is not empty

    def make_str(self,behavior=str,text=str): #crate one str out of behavior and text
        return behavior +";" +text


goosmart=Brain_Node()#Crate an run an instance of the class.