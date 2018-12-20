def chuyen_tien(money):
    assert money > 0
    print("Chuyen tien:" + str(money))
    return

chuyen_tien(10)
#chuyen_tien(-1)


try:
   fh = open("testfile", "w")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
else:
   print ("Thanh cong ghi noi dung vao file")
   fh.close()


try:
    a=10
    print (a)
    raise NameError("Hello")
except NameError as e:
		print ("Mot Exception xuat hien")
		print (e)

# Custom exception
class Networkerror(RuntimeError):
   def __init__(self, message):
        super().__init__(message)

try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print (e)