# creating Class
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        print('I am destructed', self.x)


# an = PartyAnimal()
# print('\n')
# an.party()
# an.party()
# an.party()

# PartyAnimal.party(an)

# # output is:
# # So far 1
# # So far 2
# # So far 3
# # So far 4

# print('Type: ', type(an))
# print('Dir: ', dir(an))
# print('Type: ', type(an.x))
# print('Type: ', type(an.party))
# print('\n')

# an = 42
# print('an contains', an)
# # output is:    I am destructed 4
# #               an contains 42
