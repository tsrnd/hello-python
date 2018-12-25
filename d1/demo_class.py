### demo class

#define class

class Character:
    #constructor
    def __init__(self, name, age=None):
        self.__name = name

        #private attr
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if "Riot" == name.capitalize():
            self.__name = "admin"
        else:
            self.__name = name
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    # age = property(getAge, setAge)

# test class with instance
# d = Demo("anh", 1)
# d.name = "anh"
# d.age = -2
# print(d.name)

class Skill:
    def __init__(self, skname, action=None):
        self.__skname = skname
        self.__action = action
    
    @property
    def skname(self):
        return "Skill " + self.__skname

    @skname.setter
    def skname(self, skname):
        if not isinstance(skname, str):
            raise ValueError('Skill must be string')
        self.__skname = skname

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        if not isinstance(action, str):
            raise ValueError('action must be string')
        self.__action = action

### inheritance, multi inheritance
class Yasuo(Character, Skill):
    def __init__(self, name, age=None, skillName=None):
        super().__init__(name, age)
        Skill.__init__(self, skname=skillName)
