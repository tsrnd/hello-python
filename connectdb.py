import pymysql

db = pymysql.connect('localhost', 'root', '12345678', 'db_connect')

cursor = db.cursor()

cursor.execute('select Version()')

data = cursor.fetchone()

print('Mysql version: %s' % (data))

cursor.execute('drop table if exists person')

# Create table Person
sql = """create table Person(
    ID INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(45) NULL,
    ADDRESS VARCHAR(45) NULL,
    PRIMARY KEY(ID)
)"""

cursor.execute(sql)


def get_list_person():
    con, cur = connect()
    try:
        sql = "SELECT * FROM Person"
        cur.execute(sql)
        persons = cur.fetchall()
    except pymysql.Error as e:
        print("Error:", e)
    finally:
        con.close()

    return persons

db.close()
