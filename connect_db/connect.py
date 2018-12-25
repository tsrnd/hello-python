import pymysql

db = pymysql.connect("localhost", "root", "tyhp1235", "TESTDB")

cursor = db.cursor()

cursor.execute("select Version()")

data = cursor.fetchone()

print("Mysql version: %s" % (data))

cursor.execute("drop table if exists person")

# Create table Person
sql = """create table Person(
        ID INT NOT NULL,
        NAME VARCHAR(45) NULL,
        ADDRESS VARCHAR(45) NULL,
        PRIMARY KEY(ID)
    )"""

cursor.execute(sql)

db.close()
