import pymysql


def connect_db():

    db = pymysql.connect(host='127.0.0.1', port=8889,
                         user='root', passwd='root', db='db_test')
    cursor = db.cursor()
    return db, cursor


def create_db():
    db, cursor = connect_db()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    sql = """CREATE TABLE EMPLOYEE(
        NAME CHAR(20) NOT NULL,
        AGE INT,
        ADDRESS CHAR(20) )"""
    cursor.execute(sql)
    db.close()
    return


def insert_db(name, age, address):
    db, cursor = connect_db()
    sql = """INSERT INTO EMPLOYEE(name, age, address) VALUES ('%s','%d','%s')""" % (
        name, age, address)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return


def update_db(age):
    db, cursor = connect_db()
    sql = """UPDATE EMPLOYEE SET age = %d WHERE name = 'Na'""" % (age)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return


def delete_db(age):
    db, cursor = connect_db()
    sql = """DELETE FROM EMPLOYEE WHERE age < %d""" % (age)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return


def get_list(age):
    db, cursor = connect_db()
    sql = """SELECT * FROM EMPLOYEE WHERE age > %d """ % (age)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()

    except:
        return ("Error: unable to fetch data")
    finally:
        db.close()
    return result


# create_db()
# insert_db("Na", 23, "DN")
# insert_db("Nam", 22, "QN")
# insert_db("Tam", 26, "DL")
# update_db(29)
# delete_db(23)
# print(get_list(23))
