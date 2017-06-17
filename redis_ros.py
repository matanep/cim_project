import rospy
from std_msgs.msg import String
import time
import Tkinter
import sys


class Redis():

    def __init__(self):
        self.flow = rospy.Publisher ('the_flow', String)

        self.initialize()

    def initialize(self):
        rospy.init_node('redis')


    def next(self):
        print(self.state)
        if self.state == 0:     # learn the basics
            self.set_matrix('basic')
            self.start()
            time.sleep(60)
            self.stop()
            self.state = 1
        elif self.state == 1:   # THE EXPERIMENT
            which_matrix = int(self.subject_id) % 2
            if which_matrix == 0:
                self.set_matrix('LShoulderPitch-RShoulderRoll')
            else:
                self.set_matrix('LShoulderRoll-RShoulderPitch')
            self.start()
            time.sleep(60)
            self.stop()
            self.state = 2
        elif self.state == 2:   # the tasks
            which_matrix = int(self.subject_id) % 2
            if which_matrix == 0:
                self.set_matrix('LShoulderPitch-RShoulderRoll')
            else:
                self.set_matrix('LShoulderRoll-RShoulderPitch')
            self.start()
            time.sleep(30)
            self.stop()
            self.state = 3
        elif self.state == 3:  # the tasks
            which_matrix = int(self.subject_id) % 2
            if which_matrix == 0:
                self.set_matrix('LShoulderPitch-RShoulderRoll')
            else:
                self.set_matrix('LShoulderRoll-RShoulderPitch')
            self.start()
            time.sleep(30)
            self.stop()
            self.state = 4
        elif self.state == 4:  # the tasks
            which_matrix = int(self.subject_id) % 2
            if which_matrix == 0:
                self.set_matrix('LShoulderPitch-RShoulderRoll')
            else:
                self.set_matrix('LShoulderRoll-RShoulderPitch')
            self.start()
            time.sleep(30)
            self.stop()
            self.state = 5

    def the_end(self):
        self.stop()
        self.flow.publish('the end')

    def start_experiment(self):
        self.start()
        time.sleep(60)
        self.stop()

    def set_matrix(self, which_matrix):
        self.flow.publish(which_matrix)

    def stop(self):
        self.flow.publish('stop')

    def start(self):
        self.flow.publish('start')

app = Experiment(None, int(sys.argv[1]))
print sys.argv
app.title('Experiment')
app.mainloop()


