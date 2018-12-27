import pymysql

db = pymysql.connect('localhost', 'root', '12345678', "connect_db")

cursor = db.cursor()


sql = "update Person set NAME = 'phu', ADDRESS = 'phu tran'  \
      where ID = 1"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
