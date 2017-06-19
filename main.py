import os
import threading
import time

def start_working():

    def worker1():
        os.system('python cim_project/nao_ros.py')
        return

    def worker2():
        os.system('python cim_project/brain_ros.py')
        return

    def worker3():
        os.system('python cim_project/redis_ros.py')
        return

    t1 = threading.Thread(target=worker1)
    t1.start()
    threading._sleep(0.1)
    t2 = threading.Thread(target=worker2)
    t2.start()
    threading._sleep(0.1)
    t3 = threading.Thread(target=worker3)
    t3.start()

start_working()
