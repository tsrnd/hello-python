import MySQLdb

# mo ket noi toi Database
db = MySQLdb.connect("localhost", "root", "vvudang95", "VLW")

# chuan bi mot doi tuong cursor boi su dung phuong thuc cursor()
cursor = db.cursor()

sql = "select * from categories"
try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0], " || ", row[1])
    sql = "update categories SET name = 'Phim hay' where id = %d" % (2)
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    print("Error")

# ngat ket noi voi server
db.close()
