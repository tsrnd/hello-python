import pymysql


def connectDB():
    try:
        db = pymysql.connect("localhost", "root", "", "realdb")
        return db
    except Exception as e:
        print("Error: ", e)
        return None

def createTable():  
    db = connectDB()
    cursor = db.cursor()
    sql = """CREATE TABLE SINHVIEN (
            HO  CHAR(20) NOT NULL,
            TEN  CHAR(20),
            TUOI INT,  
            GIOITINH CHAR(1),
            HOCPHI FLOAT )"""
    cursor.execute(sql)
    db.close()

def insertDB():
    db = connectDB()
    if db:
        cursor = db.cursor()
        sql = """INSERT INTO SINHVIEN(HO,
                TEN, TUOI, GIOITINH, HOCPHI)
                VALUES ('Nguyen', 'Nhat', 20, 'M', 4000000)"""
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print("error => rollback",e)
            db.rollback()
        db.close()
    else:
        print("error")

def selectDB():
    db = connectDB()
    if db:
        cursor = db.cursor()
        sql = "SELECT * FROM SINHVIEN WHERE HOCPHI > '%d'" % (1000)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            # for row in results:
            #     ho = row[0]
            #     ten = row[1]
            #     tuoi = row[2]
            #     gioitinh = row[3]
            #     hocphi = row[4]
            #     print("ho=%s,ten=%s,tuoi=%d,gioitinh=%s,hocphi=%d" %(ho, ten, tuoi, gioitinh, hocphi ))
        except Exception as e:
            print("Error: khong lay duoc du lieu",e)
        db.close()
    else:
        print("error")

def updateDB():
    db = connectDB()
    cursor = db.cursor()
    sql = "UPDATE SINHVIEN SET TEN = '%s' WHERE TEN = '%s'" % ('Nguyen','Hoang')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("error")
        db.rollback()
    db.close()

def deleteDB():
    db = connectDB()
    cursor = db.cursor()
    sql = "DELETE FROM SINHVIEN WHERE TEN = '%s'" % ('Nguyen')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("error")
        db.rollback()
    db.close()

# createTable()
# insertDB()
selectDB()

# Thuc thi truy van SQL boi su dung phuong thuc execute().
# cursor.execute("SELECT VERSION()")

# Lay mot hang boi su dung phuong thuc fetchone().
# data = cursor.fetchone()

# print("Database version : %s " % data)

# ngat ket noi voi server
