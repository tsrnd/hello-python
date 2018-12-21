# import testModule
import testModule as testM
def test(x):
    return x
print (test(5))

x = lambda a: a + 10
print(x(5))

x =  lambda a, b: a + b
print (x(5, 6))

def testLambda(x):
    return lambda a: a * x
test2 = testLambda(2)
print (test2(5))

# print ("Tong 2 so:", testModule.cong(5, 6))
# print ("Hieu 2 so:", testModule.tru(15, 29))
# print ("Tich 2 so:", testModule.nhan(12, 5))

print ("Tong 2 so:", testM.cong(5, 6))
print ("Hieu 2 so:", testM.tru(15, 29))
print ("Tich 2 so:", testM.nhan(12, 5))

f = open("hello-python/test.txt", "r")
# print("read a file :", f.read())
print("doc dong dau cua file:", f.readline())
print("doc dong thu 2 cua file:", f.readline())
# them 1 vao cuoi file
f = open("hello-python/test.txt", "a")
f.write("Now the file has one more line!")
f = open("hello-python/test.txt", "r")
print("read file :", f.read())
# viet de len file co san
f = open("hello-python/test.txt", "w")
f.write("Woops! I have deleted the content!")
f = open("hello-python/test.txt", "r")
print("read file :", f.read())
