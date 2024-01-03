from threading import Thread
from time import sleep
def hi():
    for i in range(10):
        print("Hi")
        sleep(0.5)
def hello():
    for i in range(10):
        print("Hello")
        sleep(0.5)
t1=Thread(target=hi)
t2=Thread(target=hello)
t1.start()
t2.start()
t1.join()
t2.join()
print(" The End ")