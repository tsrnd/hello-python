import pymysql


def connectDB():
    try:
        db = pymysql.connect("localhost", "root", "", "TESTDB")
        return db
    except Exception as e:
        print("Error: ", e)
        return None


def closeDB(db):
    if db.open:
        db.close()


def getVersion():
    db = connectDB()
    if(db):
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        closeDB(db)
        return data
    else:
        return "Cannot get verison"


def selectTablePeople():
    db = connectDB()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PEOPLE")
        data = cursor.fetchall()
        for row in data:
            print("id: %d   name: %s   age: %d" % (row[0], row[1], row[2]))
        closeDB(db)
    else:
        print("Cannot connect DB")


def insertPeople(name, age):
    db = connectDB()
    if(db):
        cursor = db.cursor()
        sql = "INSERT INTO PEOPLE(NAME, AGE) VALUES('%s', %d)" % (name, age)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        finally:
            db.close()
    else:
        print("Cannot connect to DB")


print("Version DB: %s" % getVersion())
selectTablePeople()
insertPeople("nhat", 17)
selectTablePeople()
