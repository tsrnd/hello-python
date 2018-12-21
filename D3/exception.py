def ChuyenKF(Nhietdo):
    assert ((Nhietdo >= 0),"Lanh hon do khong tuyet doi!")
    result = ((Nhietdo-273)*1.8) + 32
    return result

print (ChuyenKF(273))
print (int(ChuyenKF(505.78)))
print (ChuyenKF(-5))

try:
   fh = open("testfile", "r")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
else:
   print ("Thanh cong ghi noi dung vao file")


def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print ("Tham so khong chua cac so\n")
temp_convert("xyz");