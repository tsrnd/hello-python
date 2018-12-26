from threading import Thread
import time

exitFlag = 0


class myThread(Thread):
    def __init__(self, threadId, name, counter):
        Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print('Begin %s' % self.name)
        print_time(self.name, self.counter, 5)
        print('End ', self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)
thread1.start()
thread2.start()
print('End main thread')
