class animal():
    name = ''
    age = 0
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
    def show(self):
        print('My name is ' + self.name)
    def run(self):
        print('Animal running ...')
    def go(self):
        print('animal going ...')
    
class dog(animal):
    def run(self):
        print('dog running ...')


an = animal(name='Su tu', age=12)
an.show()
an.run()

cho = dog(name='cho', age=10)
cho.show()
cho.run()