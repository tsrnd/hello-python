import pytest


class CSSStudent:
    shool = 'DUT'

    def __init__(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address


def Main():
    s1 = CSSStudent("thai")
    s1.setAddress("Quang name")
    s2 = CSSStudent("quang")
    s2.setAddress("Hue")
    print(s1.getAddress())
    print(s2.getAddress())
    print(CSSStudent.shool)


if __name__ == "__main__":
    Main()
