
def division(a,b):
    try: 
        print(a / b)
        return a / b
    except:
        print("can not division")

division(1,2)
division(1,0)

def casting(a):
    try:
        return int(a)
    except:
        print("can not cast")

casting(1)
casting("123a")

def readFile():
    try:
        file = open("NoExist.txt")
        print(file)
    except:
        print("File doesn't exist")

readFile()

