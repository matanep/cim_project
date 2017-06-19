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
            behavior='Stand/Gestures/Hey_6'#todo
            if self.ulanguage=='English':
                text='Hello, welcome to the HMO. My name is Rami, and I am here to help you.Please select a language.'
            else:
                text='Hola, bienvenido a la HMO. Mi nombre es Rami, y yo estoy aqui para ayudarle. Por favor, seleccione un idioma.'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'id' in data.data:              #todo
            behavior='Stand/Gestures/Hey_6'#todo
            if self.ulanguage=='English':
                text='Please Insert your ID number.'
            else:
                text='Introduzca su numero de identificacion, Por favor.'
            pub=self.make_str(behavior,text)#make publish str
            self.robot_command.publish(pub) #publish the str in "robot_command"

        if 'invalid' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='Oh, wrong input. Please insert again'
            else:
                text='Oh, de entrada incorrecta. Por favor, inserte de nuevo'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'choice' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='Hello '+ self.name +',' + ' Please choose the requested service.'
            else:
                text='Hola '+ self.name +',' + ' por favor seleccione el servicio solicitado.'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'blood test' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='The blood test room is on the 2nd floor, on the left'
            else:
                text='La sala de examen de sangre está en el segundo piso, a la izquierda'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'vaccination' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='The vaccination room is on the 2nd floor, on the right, next to the elevator'
            else:
                text='La sala de la vacunación está en el segundo piso, a la derecha, al lado del ascensor'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'toilet' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='The toilet is on the 1st floor, on your right, next to the'
            else:
                text='El inodoro esta en el 1er piso, a la derecha, junto a la'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'reception' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='The reception is on the 1st floor, to the left'
            else:
                text='La recepción está en la primera planta, a la izquierda'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'choice2' in data.data:          #todo
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='Can I help you with anything else?'
            else:
                text='Puedo ayudarle con cualquier otra cosa?'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"

        if 'finish' in data.data:
            behavior='Stand/Gestures/Hey_6' #todo
            if self.ulanguage=='English':
                text='Thank you, and have a pleasant day!'
            else:
                text='Gracias, y tienen un día agradable!'
            pub=self.make_str(behavior,text) #make publish str
            self.robot_command.publish(pub)  #publish the str in "robot_command"



    def language(self, data):
        print 'hrhe'
        if 'english' in data.data:
            self.ulanguage='English'
            self.robot_language.publish('English')
        elif 'spanish' in data.data:
            self.ulanguage='Spanish'
            self.robot_language.publish('Spanish')
        else:
            self.ulanguage='English'
            self.robot_language.publish('English')


    def name(self,data):
        self.name=data.data

    def make_str(self,behavior=str,text=str):
        return behavior +";" +text

goosmart=Brain_Node()