import pymysql
import Object

def connect_db():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Tanh23895', db='app_database')
    cursor = db.cursor()
    return db, cursor

def select_all():
    db, cursor = connect_db()
    sql = 'SELECT * FROM CATS'
    arr = []
    try:
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        for row in result:
            cat = Object.Cat(row[1], row[2], row[3])
            arr.append(cat)
        return arr
    except Exception as err:
        db.rollback()
        raise err
    finally:
        db.close()


def insert(cat):
    db, cursor = connect_db()
    sql = "INSERT INTO CATS(name, owner, birth) VALUES('%s','%s','%s')" % (cat.name, cat.owner, cat.birth)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        db.rollback()
        raise err
    finally:
        db.close()

def update_name(id, name):
    db, cursor = connect_db()
    sql = "UPDATE CATS SET name = '%s' WHERE id = '%d'" % (name, id)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        db.rollback()
        raise err
    finally:
        db.close()

def delete(id):
    db, cursor = connect_db()
    sql = "DELETE FROM CATS WHERE id = %d" % id
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        db.rollback()
        raise err
    finally:
        db.close()
