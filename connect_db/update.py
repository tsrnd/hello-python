import pymysql

db = pymysql.connect('localhost', 'root', 'tyhp1235', "TESTDB")

cursor = db.cursor()


sql = "update Person set NAME = 'Xuan Truong', ADDRESS = 'Thai Nguyen'  \
      where ID = 6"

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
