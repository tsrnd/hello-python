import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 10)

class myThread2 (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      threadLock.acquire()
      print_time(self.name, self.counter, 5)
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 1)
thread3 = myThread2(3, "Thread-3", 2)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")