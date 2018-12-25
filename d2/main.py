from user import User
from db import connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

instance = User()
Session = sessionmaker(autoflush=False)
Session.configure(bind=connect())
ss = Session()

try:
    user1 = User(name="anh4", age=22)
    user2 = User(name="anh2", age=22)
    ss.add_all([user1, user2])

    findUser = ss.query(User).filter_by(name='anh3').first()

    findUser.name = "Anh5"
    print("check",user1 in ss)
    ss.commit()
except exc.StatementError as e:
    print("Something error: ", e)
    ss.rollback()

# print(ss.dirty)

# findUser = ss.query(User).filter_by(name='anh').first()

# findUser.name = "Anh insec every thing"
# ss.commit()

#test model
User.add(ss, {
    'name': "thatshouldoit",
    'age': 22
})
user = ss.query(User).filter_by(name="anh").first()
user.update(ss, {
    'name': 'hihi',
    'age': 22
})