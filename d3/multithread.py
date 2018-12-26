import time, threading

def call_quare(number):
    for i, v in enumerate(number):
        time.sleep(0.5)
        print("Test1:", i+1, v ** 2)
        
def call_cube(number):
    for i, v in enumerate(number):
        time.sleep(0.6)
        print("Test2:", i+1, v ** 3)
        
arr = [2, 3, 1, 5, 1, 2, 5, 7]

t = time.time()
# call_quare(arr)
# call_cube(arr)
# t1 = threading.Thread(target=call_quare, args=(arr,))
# t2 = threading.Thread(target=call_cube, args=(arr,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
print("DONE", time.time() - t)

### inheritance from threading
class Demo(threading.Thread):
    def __init__(self, counter, delay):
        super(Demo, self).__init__()
        self.counter = counter
        self.delay = delay
    
    def run(self):
        for i in range(self.counter):
            print("Index at: ", i)
            time.sleep(self.delay)

demo = Demo(10, 1)
# demo.start()

### demo deadlock handle
lock = threading.Lock()
lSync = []
lAsync = []

class TestDeadlock(threading.Thread):
    def __init__(self, isActive = False, list=[]):
        super(TestDeadlock, self).__init__()
        self.list = list
        if isActive:
            self.__isActive = True
            self.lock = threading.Lock()
        else:
            self.__isActive = False

    def run(self):
        if self.__isActive:
            lock.acquire()
            for i in range(4):
                time.sleep(0.2)
                self.list.append(i)
            lock.release()
        else:
            for i in range(4):
                time.sleep(0.2)
                self.list.append(i)

dtA1 = TestDeadlock(isActive=False, list=lAsync)
dtA2 = TestDeadlock(isActive=False, list=lAsync)
dtA1.start()
dtA2.start()
dtA1.join()
dtA2.join()

dt1 = TestDeadlock(isActive=True, list=lSync)
dt2 = TestDeadlock(isActive=True, list=lSync)
dt1.start()
dt2.start()
dt1.join()
dt2.join()

print(lAsync)
print(lSync == sorted(lSync))
    