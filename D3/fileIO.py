
# import math
str = input("Nhap dau vao cua ban: ")
print ("Dau vao da nhan la : ", str)

page = int(input("Nhap so trang ban dang dọc: "))
word = input("Nhap tu ban dang nghi: ")
number = int(input("Nhap so tu 1 den 100000 ma ban dang doan': "))
name = 'Lee.Wuan.Jain'

print ('Page = ', page)
print ('Word = ', word)
print ('Number = ', number)
print ('name + word = ', name, word)
print (page + number)

openFile = open('text.txt', 'w')
openFile.write("Rồi về già lặng lẽ ăn mì tôm mới đúng hơn haha")
openFile.close()
obj1 = open("text.txt","r")
s = obj1.read()
print (s)
obj1.close()
obj2 = open("text.txt","r")
s1 = obj2.read(20)
print (s1)
obj2.close()


fo = open("text.txt", "wb")
print ("Ten cua file la: ", fo.name)
print ("File da duoc dong hay chua : ", fo.closed)
print ("Che do mode la : ", fo.mode)
# print ("Softspace la : ", fo.softspace)