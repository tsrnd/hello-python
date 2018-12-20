### variable accessing

a = "test"

def assignA():
    global a
    a = a + "nope"

print("before: ",a)
assignA()
print("after: ", a)


# function in function
victim = "wow"
def test1():
    victim = "what"
    def test2():
        global victim
        victim = "who iam i?"
    
    test2()
    print(victim)

test1()

print(victim)

# non-local
victim = "wow"
def test3():
    victim = "what"
    def test2():
        nonlocal victim
        print("locals variable: %s, %s" %(locals(), locals()['victim']))
        victim = "who iam i?"
    
    test2()
    print("---local is: %s\n---global is: %s" %(locals(), globals()))
    print(victim)

test3()

print(victim)


### test import module
from d3module import number, file, vandap

# call this twice when import module
# importlib.reload(m)
# print(dir(m))
# m.test()
print(number.checkPrime(7))

###get file

helloTXT = file.openFile('./d3module/test/hello.txt', 'r+')
print(helloTXT.read())
print("This file is current %s edit\nand position is %d" %("can" if helloTXT.writable() else "cannot", helloTXT.tell()))
helloTXT.write("\nwhat should i do now?")
print(["This file can seek?"], helloTXT.seekable())
helloTXT.seek(11, 0)
print(helloTXT.readlines()[-1])

###bebin chat
# vandap.sendRequest()
