class HCN :
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def getarea(self):
        return self.height * self.width
