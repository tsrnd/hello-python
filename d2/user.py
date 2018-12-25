from sqlalchemy import Column, Integer, String, exc
from sqlalchemy.ext.declarative import declarative_base
from db import connect

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(Integer)

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def add(cls, ss, data):
        try:
            ss.add(cls(name=data['name'], age=data['age']))
            ss.commit()
        except exc.DatabaseError as e:
            print("Somthing error: ", e)


    def update(self, ss, data):
        try:
            self.name = data['name']
            self.age = data['age']
            ss.commit()
        except exc.DatabaseError as e:
            print("Update error", e)

Base.metadata.create_all(connect())
