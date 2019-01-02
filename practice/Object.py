import day2_database as db


class Cat:

    def __init__(self, name, owner, birth):
        self.name = name
        self.owner = owner
        self.birth = birth

# -------------------------------------------#


def display_all():
    try:
        arr = db.select_all()
        for e in arr:
            print('name: {0}, owner: {1}, birth: {2}'.format(
                e.name, e.owner, e.birth))
    except Exception as err:
        print(err)


def insert(cat):
    try:
        db.insert(cat)
    except Exception as err:
        print(err)

def update_name(id, name):
    try:
        db.update_name(id, name)
    except Exception as err:
        print(err)

def delete(id):
    try:
        db.delete(id)
    except Exception as err:
        print(err)