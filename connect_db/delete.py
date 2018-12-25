import pymysql

db = pymysql.connect('localhost', 'root', 'tyhp1235', 'TESTDB')

cursor = db.cursor()

sql = "delete from Person where ID = 7 "

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
