import pymysql


def db_connect():
    # Open database connection
    db_connect = pymysql.connect(
        db="management_user",
        user="root",
        passwd="root",
        host="localhost",
        port=8889
    )
    db_cursor = db_connect.cursor()
    return db_connect, db_cursor


def del_table():
    db, cursor = db_connect()
    cursor._defer_warnings = True
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    return


def create_table():
    db, cursor = db_connect()
    sql_create = """CREATE TABLE EMPLOYEE (
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT )"""

    cursor.execute(sql_create)
    db.close()
    return


def query_insert():
    db, cursor = db_connect()
    sql_insert = """INSERT INTO EMPLOYEE(FIRST_NAME,
        LAST_NAME, AGE, SEX, INCOME)
        VALUES ('Mac', 'Mohan', 20, 'M', 2000),('Tram','Pham',23,'M',2001)
        """
    try:
        # Execute the SQL command
        cursor.execute(sql_insert)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    finally:
        db.close()
    return


def query_select():
    db, cursor = db_connect()
    sql_select = "SELECT * FROM EMPLOYEE WHERE AGE < '%d'" % (25)
    try:
        cursor.execute(sql_select)
        results = cursor.fetchall()
        # for row in results:
        #     fname = row[0]
        #     lname = row[1]
        #     age = row[2]
        #     sex = row[3]
        #     income = row[4]
        #     # Now print fetched result
        #     return("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %
        #            (fname, lname, age, sex, income))
    except:
        return("Error: unable to fecth data")
    finally:
        db.close()
    return results


del_table()
create_table()
query_insert()
results = query_select()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # Now print fetched result
    print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %
          (fname, lname, age, sex, income))
