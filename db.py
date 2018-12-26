import pymysql

# Open database connection
db = pymysql.connect("localhost","root","mypass","test_db" )
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,  
    SEX CHAR(1),
    INCOME FLOAT )"""
cursor.execute(sql)

sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000), ('Bill', 'Potter', 25, 'S', 2000)"""
try:
    # Execute the SQL command
    cursor.execute(sql2)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

sql3 = """SELECT * FROM EMPLOYEE"""
cursor.execute(sql3)
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # Now print fetched result
    print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
        (fname, lname, age, sex, income ))

sql4 = "UPDATE EMPLOYEE SET AGE = 21 WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql4)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
# disconnect from server

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (24)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

db.close()
