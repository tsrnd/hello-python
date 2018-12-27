import pymysql

db = pymysql.connect("localhost", "root", "12345678", "db_connect")

cursor = db.cursor()


# Insert into Person

sql = """INSERT INTO Person (NAME, ADDRESS)
        VALUES ('phu', 'da nang');
        """
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


sql2 = "select * from Person"
try:
    cursor.execute(sql2)
    result = cursor.fetchall()
    for row in result:
        id = row[0]
        name = row[1]
        address = row[2]
        print("ID = %d, Name = %s, Address = %s" % (id, name, address))
except:
    db.rollback()
db.close()
