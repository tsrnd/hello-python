import pymysql
import logging


def create_connect():
    db = pymysql.connect(
        db='qlsv',
        user='root',
        passwd='root',
        host='localhost',
        port=8889)
    return db


def create_data(name, email):
    db = create_connect()
    cur = db.cursor()
    sql = "INSERT INTO sinhvien(ten,email) VALUES (%s, %s)"
    try:
        cur.execute(sql, (name, email))
        db.commit()
    except pymysql.DatabaseError as error:
        db.rollback()
        logging.error(error)
    finally:
        db.close()


def select_data():
    db = create_connect()
    cur = db.cursor()
    sql = "SELECT * FROM sinhvien"
    try:
        cur.execute(sql)
    except pymysql.DatabaseError as error:
        logging.error(error)
    else:
        rows = cur.fetchall()
        for row in rows:
            print("{0:3} {1:>10}".format(row[0], row[2]))


def update_data(id_sv, email):
    db = create_connect()
    cur = db.cursor()
    sql = "UPDATE sinhvien SET email = %s WHERE id = %s"
    try:
        cur.execute(sql, (email, id_sv))
        db.commit()
    except pymysql.DatabaseError as error:
        logging.error(error)
    finally:
        db.close()


create_data('Tam', 'tam@gmail.com')
select_data()
update_data(1, 'tam1@gmail.com')
select_data()
