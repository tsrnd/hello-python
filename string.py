hello = "hello"
print(hello[1:3])
print(hello[1])
print("hello %s %i do %c" %("python",1,"c"))
print(*"hello")
print("capitalize "+hello.capitalize())
print("center : "+ hello.center(40,'a'))

str = "this is string example....wow!!!"
sub = "i"
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,str.__len__()))

suffix = 'exam'
print (str.endswith(suffix))
print (str.endswith(suffix, 0, 19))

str = "this is\tstring example....wow!!!"
print(str[5])
print ("Double exapanded tab: " +  str.expandtabs(4))
print(str.title())
print(str.title().swapcase())

str = "this is \nstring example....\nwow!!!"
print (str.splitlines( ))
