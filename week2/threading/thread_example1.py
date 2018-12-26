from threading import Thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))


try:
    Thread(target=print_time, args=("Thread 1", 2)).start()
    Thread(target=print_time, args=("Thread 2", 4)).start()
except Exception as e:
    print("Error: Cannot starting thread")
