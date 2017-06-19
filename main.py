import os
import threading
import time

def start_working():

    def worker1():
        os.system('python nao_ros.py')
        return

    def worker2():
        os.system('python brain_ros.py')
        return

    def worker3():
        os.system('python redis_ros.py')
        return

    t1 = threading.Thread(target=worker1)
    t1.start()
    threading._sleep(0.5)
    t2 = threading.Thread(target=worker2)
    t2.start()
    threading._sleep(0.5)
    t3 = threading.Thread(target=worker3)
    t3.start()

start_working()
