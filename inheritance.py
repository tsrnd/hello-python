# import the PartyAnimal class from file classes_objects

from classes_objects import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))

# output are:
# Sally constructed
# Sally party count 1
# Jim constructed
# Jim party count 1
# Jim party count 2
# Jim points 6
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__','__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'party', 'points', 'six', 'x']
# I am destructed 1
# I am destructed 2
