import time, random
from threading import Lock, Thread, Event, RLock, Semaphore, Condition

print('######################################')
print('Use Event')
g = 0
event = Event()
event1 = Event()
#  add_one wait add_three
def add_one():
   event.wait()
   print("begin add_one")
   global g
   g += 1
   time.sleep(1)
   print("g = ",g)
   event.clear()
   event1.set()

#  add_two wait add_one
def add_two():
   event1.wait()
   print("begin add_two")
   global g
   g += 2
   time.sleep(1)
   print("g = ",g)
   event1.clear()
   
def add_three():
   print("begin add_three")
   global g
   g += 3
   time.sleep(1)
   print("g = ",g)
   event.set()

threads = []
for func in [add_one, add_two, add_three]:
   threads.append(Thread(target=func))
   threads[-1].start()

# the last print wait 3 thread
for thread in threads:
   thread.join()
print(g)

print('######################################')
print('Use Lock')
lock = Lock()
lock1 = Lock()
g = 0
#  add_one_lock wait add_three_lock
def add_one_lock():
   lock.acquire()
   print("begin add_one_lock")
   global g
   g += 1
   time.sleep(1)
   print("g = ",g)
   lock.release()
   lock1.release()

#  add_two_lock wait add_one_lock
def add_two_lock():
   lock1.acquire()
   print("begin add_two_lock")
   global g
   g += 2
   time.sleep(1)
   print("g = ",g)
   lock1.release()
   
def add_three_lock():
   print("begin add_three_lock")
   global g
   g += 3
   time.sleep(1)
   print("g = ",g)
   lock.release()

threads = []
lock.acquire()
lock1.acquire()

for func in [add_one_lock, add_two_lock, add_three_lock]:
   threads.append(Thread(target=func))
   threads[-1].start()

# the last print wait 3 thread
for thread in threads:
   thread.join()
print(g)

print('######################################')
print('Use RLock to un-block itself thread take lock before (usually use for recursion)')
rlock = RLock()
number = 0
rlock.acquire()
number += 3
rlock.acquire() # This won’t block.
number += 4
rlock.release()
rlock.release()
print("number is ", number)
lastResult = 0
def sumN(n):
    global lastResult
    rlock.acquire()
    if n == 1:
        lastResult = 1
    else:
        lastResult = sumN(n-1)+n
    rlock.release()
    return lastResult
def lastResultAddOne():
    rlock.acquire()
    global lastResult
    lastResult += 1
    rlock.release()
t1 = Thread(target=sumN, kwargs=dict(n=5))
t2 = Thread(target=lastResultAddOne)
t1.start()
t2.start()
t1.join()
t2.join()
print("last result is ", lastResult)

print('######################################')
print('Use Semaphore to limit thread')
limitSema = 10
se = Semaphore(value=limitSema)
def countLimitSemaphore(i):
    se.acquire()
    time.sleep(3)
    print("time is", time.strftime("%H:%M:%S", time.localtime()), " with i = ", i)
    se.release()
threads = []
print("See 10 thread run and sleep 3s and the 10 next thread run, so on ...")
for i in range(0, 30):
    threads.append(Thread(target=countLimitSemaphore, kwargs=dict(i = i)))
    threads[-1].start()
for thread in threads:
   thread.join()

print('######################################')
print('Use Condition')
condition = Condition()
listProduct = []
countPro = 0
countUse = 0
# product 5 items
def product():
    print("Begin product")
    global countPro
    while countPro < 5:
        countPro += 1
        condition.acquire()
        number = random.randint(0, 256)
        time.sleep(2)
        listProduct.append(number)
        print(f"Product {number}")
        condition.notify()
        condition.release()
        time.sleep(1)
    print("_____end product_____")
# use 3 items
def use():
    print("Begin use")
    global countUse
    while countUse < 3:
        countUse += 1
        condition.acquire()
        while not listProduct:
            print("List product empty => wait for product")
            # during wait will free lock for product use
            condition.wait()
        print(f"Use {listProduct.pop(0)}")  
        condition.release()
    print("_____end use_____")

t1 = Thread(target=product)
t2 = Thread(target=use)
t2.start()
t1.start()
t1.join()
t2.join()