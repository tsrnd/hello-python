from multithread import TestDeadlock

#test  dead
def testAsync():
    check = []
    instance1 = TestDeadlock(False, check)
    instance2 = TestDeadlock(False, check)
    instance1.start()
    instance2.start()
    instance1.join()
    instance2.join()
    print(check)
    assert check == sorted(check)

def testSync():
    check = []
    instance1 = TestDeadlock(True, check)
    instance2 = TestDeadlock(True, check)
    instance1.start()
    instance2.start()
    instance1.join()
    instance2.join()
    assert check != sorted(check)
    