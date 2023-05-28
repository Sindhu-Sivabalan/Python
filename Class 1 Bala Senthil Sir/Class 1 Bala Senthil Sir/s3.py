import threading
import datetime
import time


def something():
    while True:
        print(datetime.datetime.now())
        time.sleep(1)


def show():
    for i in range(50):
        print(i)
        time.sleep(1)


x=threading.Thread(target=something)
x.start()
show()