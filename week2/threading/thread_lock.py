import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print('Begin %s' % self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 1)
thread3 = myThread(3, 'Thread-3', 1)
thread1.start()
thread2.start()
thread3.start()
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
for t in threads:
    print('join ', t.getName())
    t.join()
print('Exitting Main Thread')
