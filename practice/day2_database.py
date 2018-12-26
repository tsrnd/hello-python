import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='Tanh23895', db='app_database')

cursor = db.cursor()

sql = "select * from cats"
try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0], " || ", row[1], " || ", row[2], " || ", row[3])
    sql = "update cats SET name = 'Tanhle' where id = {}".format(2)
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    print("Error")

db.close()
