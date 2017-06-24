#Imports:
import os
import threading
import time

#make sure you have redis and ros running before you run the code

#This function will run all files for the system to work:
def start_working():

    def worker1():
        os.system('python nao_ros.py')  #nao_ros
        return

    def worker2():
        os.system('python brain_ros.py')#brain_ros
        return

    def worker3():
        os.system('python redis_ros.py')#redis_ros
        return

    t1 = threading.Thread(target=worker1) #thread
    t1.start()#run file
    threading._sleep(0.5)#Wait between files
    t2 = threading.Thread(target=worker2)#thread
    t2.start()#run file
    threading._sleep(0.5)#Wait between files
    t3 = threading.Thread(target=worker3)#thread
    t3.start()#run file

start_working()#start function
