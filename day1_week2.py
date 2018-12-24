import re, random, string
print('############################################')
print('Class Object kind property, type func')
class MyClass:
    publicSound = _protectSound = __privateSound = ''
    def __init__(self, sound=None):
        if sound != None:
            self.publicSound = sound
            self._protectSound = sound[:10]
            self.__privateSound = sound[:5]
    def isMatchRegex(self, regex):
        if re.match(regex, self.publicSound):
            return True
        return False
    def setPrivateSound(self, sound):
        self.__privateSound = sound
    def getPrivateSound(self):
        return self.__privateSound
    @classmethod
    def nameClass(cls):
        return cls
    @staticmethod
    def randomSound(n):
        return ''.join([random.choice(string.ascii_letters.join(['-', '_'])) for _ in range(n)])

class ChildMyClass(MyClass):
    # override __init__ func
    def __init__(self, sound=None):
        MyClass.__init__(self, sound)
        if sound == None:
            self.publicSound = ChildMyClass.randomSound(10)
            self._protectSound = self.publicSound[:10]
            self.setPrivateSound(self.publicSound[:5])
        print (f'Name of parent class is {MyClass.nameClass()} and current class is {ChildMyClass.nameClass()}')
        print(f"Public sound is {self.publicSound}")
        print(f"Protect sound is {self.publicSound}")
        print(f"Private sound is {self.getPrivateSound()}")
ch1 = ChildMyClass()
ch2 = ChildMyClass("Ha1-x_")
print(ch1.isMatchRegex(r'^[a-zA-Z0-9\-_]*$'))
print(ch2.isMatchRegex(r'^[a-zA-Z0-9\-_]*$'))
    
print('############################################')
print('Regex patern')
print("Split by regex [^a-zA-Z]* has ", re.split('[^a-zA-Z]*', 'ht12y@gmail..com'))
print("Split by regex [^a-zA-Z]+ has ", re.split('[^a-zA-Z]+', 'ht12y@gmail..com'))
print("Split by regex [^a-zA-Z] has ", re.split('[^a-zA-Z]', 'ht12y@gmail..com'))
print("Remove non character in first string has ", re.split('^[^a-zA-Z]+', '877((8882ht12y@gmail..com')[1])
print("Remove non character in end string has ", re.split('[^a-zA-Z]+$', 'ht12y@gmail..com56221&&&')[0])

print('(foo.)+  match in --foo1foo2-- is ',re.match('(foo.)+', '--foo1foo2--'))
# use search if find contain middle string
print('foo. search in --foo1foo2-- is ',re.search('foo.', '--foo1foo2--'))
print('(foo.)+  search in --foo1foo2-- is ',re.search('(foo.)+', '--foo1foo2--'))
print('(foo.)+$ search in --foo1foo2 is ',re.search('(foo.)+$', '--foo1foo2'))

print('(foo.)+$ search in --foo1\\nfoo2 is ',re.search('(foo.)+$', '--foo1\nfoo2'))
print('(foo.)+$ search multiline mode in --foo1\\nfoo2 is ',re.search('(foo.)+$', '--foo1\nfoo2', re.M))

print('foo.$ findall in --foo1\\nfoo2 is ',re.findall('foo.$', '--foo1\nfoo2'))
print('foo.$ findall multiline mode in --foo1\\nfoo2 is ',re.findall('foo.$', '--foo1\nfoo2', re.M))

# group (?P<name>) and (?P=name)
m = re.search(r"(?P<first_name>\w+) (?P<last_name>\w+) (?P=last_name)", "@H TY TY")
print('fisrt name', m.group('first_name'))
print('last name', m.group('last_name'))
# (?!...)
print("AB match A if follow is not B", re.match('A(?!B)', 'Ac'))
# (?=...)
print("AB match A if follow is B", re.match('A(?=B)', 'AB'))
# (?<=...)
print("Search all substring follow - and be followed by - is: ", re.search('(?<=-)[^_]+', 'one-two_three').group(0))
