import pymysql

db = pymysql.connect("localhost", "root", "tyhp1235", "TESTDB")

cursor = db.cursor()


# Insert into Person

sql = """INSERT INTO Person (ID, NAME, ADDRESS)
        VALUES ('7', 'Thai', 'da nang');
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
