import pymysql

db_info = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "port": 8889,
    "database": "test_py",
}


def connect():
    try:
        con = pymysql.connect(
            db=db_info["database"], user=db_info["user"], passwd=db_info["password"], host=db_info["host"], port=db_info["port"]
        )
    except Exception as e:
        print("Error:", e)
    else:
        cur = con.cursor()
    return con, cur


def insert_student(name, age, clas):
    con, cur = connect()
    try:
        sql = """INSERT INTO student(name,age,class)
                VALUES('%s',%s,'%s')""" % (name, age, clas)
        if cur.execute(sql) == 1:
            user_id = cur.lastrowid

    except Exception as e:
        print("Error:", e)
    else:
        con.commit()
    finally:
        con.close()

    return user_id


def get_list_student():
    con, cur = connect()
    sql = "SELECT * FROM student"
    try:
        cur.execute(sql)
    except Exception as e:
        print("Error:", e)
    else:
        students = cur.fetchall()
    finally:
        con.close()

    return students


def get_student_by_id(id):
    con, cur = connect()
    try:
        sql = "SELECT * FROM student WHERE id = {}".format(id)
        cur.execute(sql)
        student = cur.fetchall()
    except Exception as e:
        print("Error:", e)
    finally:
        con.close()

    return student


def update_student(id, name, age, clas):
    con, cur = connect()
    try:
        sql = """UPDATE student SET name = '%s', age = %s, class = '%s' WHERE id = '%s'""" % (
            name, age, clas, id)
        cur.execute(sql)

    except Exception as e:
        print("Error:", e)
    else:
        con.commit()
    finally:
        con.close()
    return id


# print(update_student(6, "minh leo", "24", "13T1"))
print(get_list_student())
# print(get_student_by_id(1))
# for row in rows:
# print("{0} {1} {2}".format(row[0], row[1], row[2]))

# con, cur = connect()
# cur.execute("SELECT VERSION()")

# version = cur.fetchone()

# print("Database version: {}".format(version[0]))
