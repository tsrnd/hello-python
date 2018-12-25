import pymysql

# mo ket noi toi Database
db = pymysql.connect("localhost","root","quangtrangle96","TESTDB" )

# chuan bi mot doi tuong cursor boi su dung phuong thuc cursor()
cursor = db.cursor()

# Chuan bi truy van SQl de INSERT mot ban ghi vao trong database.
sql = "SELECT * FROM SINHVIEN \
       WHERE HOCPHI > '%d'" % (1000)
try:
   # Thuc thi lenh SQL
   cursor.execute(sql)
   # Lay tat ca cac hang trong list.
   results = cursor.fetchall()
   for row in results:
      ho = row[0]
      ten = row[1]
      tuoi = row[2]
      gioitinh = row[3]
      hocphi = row[4]
      # Bay gio in ket qua
      print ("ho=%s,ten=%s,tuoi=%d,gioitinh=%s,hocphi=%d" % \
            (ho, ten, tuoi, gioitinh, hocphi ))
except:
   print ("Error: khong lay duoc du lieu")

# ngat ket noi voi server
db.close()