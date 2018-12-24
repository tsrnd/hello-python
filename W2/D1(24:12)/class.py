class Sinhvien:
    'Class co so chung cho tat ca sinh vien'
    svCount = 0
    # age = 0

    def __init__(self, ten, hocphi):
        self.ten = ten
        self.hocphi = hocphi
        Sinhvien.svCount += 1
   
    def displayCount(self):
        print ("Tong so Sinh vien %d" % Sinhvien.svCount)

    def displaySinhvien(self):
        # print(getattr(self, 'age'))
        print ("Ten : ", self.ten,  ", Hoc phi: ", self.hocphi)


sv1 = Sinhvien('Quoc Anh', -2000000)
sv2 = Sinhvien('Quang Trang', 35000000)
# sv1.displayCount()
sv1.displaySinhvien()
print ('Tong so sinh vien: ', Sinhvien.svCount)

sv2.age = 22
sv2.displaySinhvien()
print(getattr(sv2, 'age'))

if (hasattr(sv2, 'age')) : print ('Sv2 has age u has been input')
else : print ('Sv2 has NOT age u has been input')

if (hasattr(sv1, 'age')) : print ('Sv1 has age u has been input')
else : print ('Sv1 has NOT age u has been input')

setattr(sv2, 'sex', 'Less')
print('Sex of sv2 is: ', getattr(sv2, 'sex'))

delattr(sv2, 'age')

if (hasattr(sv2, 'age')) : print ('Sv2 has been deleted age by u')
else : print ('Sv2 has been exist')

print ("Sinhvien.__doc__:", Sinhvien.__doc__)
print ("Sinhvien.__name__:", Sinhvien.__name__)
print ("Sinhvien.__module__:", Sinhvien.__module__)
print ("Sinhvien.__bases__:", Sinhvien.__bases__)
print ("Sinhvien.__dict__:", Sinhvien.__dict__)