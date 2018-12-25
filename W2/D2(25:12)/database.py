import pymysql

# mo ket noi toi Database
db = pymysql.connect("localhost","root","quangtrangle96","TESTDB" )

# chuan bi mot doi tuong cursor boi su dung phuong thuc cursor()
cursor = db.cursor()

# Thuc thi truy van SQL boi su dung phuong thuc execute().
cursor.execute("SELECT VERSION()")

# Lay mot hang boi su dung phuong thuc fetchone().
data = cursor.fetchone()

print ("Database version : %s " % data)

# Tao mot bang
sql = """CREATE TABLE GIANGVIEN (
         HO  CHAR(20) NOT NULL,
         TEN  CHAR(20),
         TUOI INT,  
         GIOITINH CHAR(1),
         MUCLUONG FLOAT )"""

insert = """INSERT INTO SINHVIEN(ID, HO,
         TEN, TUOI, GIOITINH, HOCPHI)
         VALUES (1, 'Lee', 'Wuan.Jain', 22, 1, 4000000)"""

# cursor.execute(insert)
try:
   # Thuc thi lenh SQL
   cursor.execute(insert)
   # Commit cac thay doi vao trong Database
   db.commit()
except:
   # Rollback trong tinh huong co bat ky error nao
   db.rollback()
# ngat ket noi voi server
db.close()


