def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

try:
   fh = open("testfile", "w")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print("Error: Khong tim thay file")
else:
   print("Thanh cong ghi noi dung vao file")
   fh.close()


try:
   fh = open("testfile", "r")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print("Error: Khong tim thay file")
else:
   print("Thanh cong ghi noi dung vao file")
