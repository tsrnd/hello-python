import pymysql

db = pymysql.connect("localhost","root","","realdb" )
cursor = db.cursor()
sql = """CREATE TABLE SINHVIEN (
         HO  CHAR(20) NOT NULL,
         TEN  CHAR(20),
         TUOI INT,  
         GIOITINH CHAR(1),
         HOCPHI FLOAT )"""
# cursor.execute(sql)

sql = """INSERT INTO SINHVIEN(HO,
         TEN, TUOI, GIOITINH, HOCPHI)
         VALUES ('Nguyen', 'Nhat', 20, 'M', 4000000)"""
try:
   cursor.execute(sql)
   # Commit cac thay doi vao trong Database
   db.commit()
except:
   print("error => rollback")
   db.rollback()

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
      print("ho=%s,ten=%s,tuoi=%d,gioitinh=%s,hocphi=%d" %(ho, ten, tuoi, gioitinh, hocphi ))
except:
   print("Error: khong lay duoc du lieu")

sql = "UPDATE SINHVIEN SET TEN = '%s' WHERE TEN = '%s'" % ('Nguyen','Hoang')
try:
    cursor.execute(sql)
    db.commit()
except:
    print("error")
    db.rollback()

sql = "DELETE FROM SINHVIEN WHERE TEN = '%s'" % ('Nguyen')
try:
    cursor.execute(sql)
    db.commit()
except:
    print("error")
    db.rollback()

db.close()

# Thuc thi truy van SQL boi su dung phuong thuc execute().
# cursor.execute("SELECT VERSION()")

# Lay mot hang boi su dung phuong thuc fetchone().
# data = cursor.fetchone()

# print("Database version : %s " % data)

# ngat ket noi voi server
