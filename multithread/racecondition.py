import threading

# global x
x = 0


def increament():
    global x
    x += 1


def doingthread(lock):
    for _ in range(100000):
        lock.acquire()
        increament()
        lock.release()


def Main():
    global x
    x = 0

    # creating a lock
    lock = threading.Lock()

    t1 = threading.Thread(target=doingthread, args=(lock,))
    t2 = threading.Thread(target=doingthread, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        Main()
        print("Iteration {0} , x = {1}".format(i, x))
