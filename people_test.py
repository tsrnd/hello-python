from people import People,Nhat
import unittest

class PeopleTest(unittest.TestCase):
    def testGetName(self):
        people = Nhat("nhat",23)
        assert people.getName() == "nhat"

    def testGetId(self):
        people = People("nhat",23)
        assert people.getId() == 4

