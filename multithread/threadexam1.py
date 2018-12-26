import threading
import os


def task1():
    print("Task1 assigned to thread: {}".format(
        threading.current_thread().getName()))
    print("ID of process running task1: {}".format(os.getpid()))


def task2():
    print("Task2 assigned to thread: {}".format(
        threading.current_thread().getName()
    ))

    print("ID of proecess running task2: {}".format(os.getpid()))


if __name__ == "__main__":
    print("Id of process running main program: {}".format(os.getpid()))

    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=task1(), name="T1")
    t2 = threading.Thread(target=task2(), name="T2")

    t1.start()
    t2.start()
    t1.join()
    t2.join()
