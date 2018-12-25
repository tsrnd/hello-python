from sqlalchemy import create_engine

def connect():
    try:
        connStr = "mysql+pymysql://root:root@localhost/python_app_1"
        return create_engine(connStr)
    except Exception as e:
        print("Something error: ", e)